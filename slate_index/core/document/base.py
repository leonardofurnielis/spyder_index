import os
import uuid
import mimetypes
from typing import TYPE_CHECKING, Literal
from datetime import datetime
from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from llama_index.core.schema import Document as LlamaIndexDocument
    from langchain_core.documents import Document as LangchainDocument

class Document(BaseModel):
    doc_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    text: str = Field(default="")
    metadata: dict = Field(default={})

    @classmethod
    def class_name(cls) -> str:
        return "Document"

    def set_content(self, text: str, metadata: dict = {}) -> None:
        """Set the text content of the document."""
        self.text = text
        self.metadata = metadata

    def get_text(self) -> str:
        return self.text
    
    def get_metadata(self) -> dict:
        return self.metadata
    
    @classmethod
    def _parse_metadata(cls, metadata: dict, framework: Literal["llama_index", "langchain"]) -> dict:
        _metadata: dict = {}
        today = datetime.now()

        if framework == "llama_index":
            _metadata["page"] = metadata["page_label"]
            _metadata["file_name"] = metadata["file_name"]
            _metadata["file_type"] = metadata["file_type"]
            _metadata["creation_date"] = "%s-%s-%s" % (today.year, today.month, today.day)

        if framework == "langchain":
            _metadata["page"] = metadata["page"] + 1
            _metadata["file_name"] = os.path.basename(metadata["source"])
            _metadata["file_type"] = mimetypes.guess_type(_metadata["file_name"])[0]
            _metadata["creation_date"] = "%s-%s-%s" % (today.year, today.month, today.day)

        return _metadata
    
    @classmethod
    def _from_langchain_format(cls, doc: "LangchainDocument") -> "Document":
        """Convert struct from LangChain document format."""
        
        parsed_metadata = cls._parse_metadata(doc.metadata, "langchain")
        return cls(text=doc.page_content, metadata=parsed_metadata)
    
    @classmethod
    def _from_llama_index_format(cls, doc: "LlamaIndexDocument") -> "Document":
        """Convert struct from LangChain document format."""

        parsed_metadata = cls._parse_metadata(doc.metadata, "llama_index")
        return cls(text=doc.text, metadata=parsed_metadata)