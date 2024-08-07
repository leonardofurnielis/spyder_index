import numpy as np
from typing import Literal, List, Dict

from spyder_index.core.embeddings import BaseEmbedding

from pydantic.v1 import BaseModel


class KnowledgeBaseCoverage(BaseModel):
    """Indicates how much the KnowledgeBase has contributed to the answer's coverage.
    If the LLM response contains information from the KnowledgeBase, this percentage is going to be very high.

    Args:
        embed_model (BaseEmbedding): Embedding model to use.
        similarity_mode (str, optional): The similarity strategy. Defaults to ``cosine``.
        similarity_threshold (float, optional): Embedding similarity threshold for "passing". Defaults to ``0.8``.
    """

    embed_model: BaseEmbedding
    similarity_mode: Literal["cosine", "dot_product", "euclidean"] = "cosine"
    similarity_threshold: float = 0.8

    class Config:
        arbitrary_types_allowed = True

    def evaluate(self, contexts: List[str], output: str) -> Dict:
        """
        Args:
            contexts (str): List of Strings used as LLM context.
            output (str): The LLM response based on given context.
        """

        if not contexts or not output:
            raise ValueError("Must provide these parameters [`contexts`, `output`]")

        coverage = {"contexts_score": [], "score": 0}
        output_embedding = self.embed_model.get_query_embedding(output)

        for context in contexts:
            context_embedding = self.embed_model.get_query_embedding(context)
            coverage["contexts_score"].append(
                self.embed_model.similarity(output_embedding, context_embedding, mode=self.similarity_mode))

        coverage["score"] = np.mean(coverage["contexts_score"])
        coverage["passing"] = coverage["score"] >= self.similarity_threshold

        return coverage
