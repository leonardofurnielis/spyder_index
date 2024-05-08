# Spyder Index

## Table of Contents

- Embeddings
  - [HuggingFace](#embeddings-huggingface)
- Ingestion
  - [Directory Files](#ingestion-directory-files)
  - [IBM COS](#ingestion-ibm-cloud-object-store-s3)
- Text Splitter
  - [Semantic Splitter](#text-splitter-semantic-splitter)
  - [Sentence Splitter](#text-splitter-sentence-splitter)
- Vector Store
  - [Elasticsearch](#vector-store-elasticsearch)

## Embeddings: HuggingFace

### Overview
Class for computing text embeddings using HuggingFace models.

### API Reference

##### **`HuggingFaceEmbeddings(model_name: str= "sentence-transformers/all-MiniLM-L6-v2", device: Literal["cpu", "cuda"] = "cpu")`**

Initialize a HuggingFaceEmbeddings object.

- `model_name` (str, optional): Name of the HuggingFace model to be used. Defaults to "sentence-transformers/all-MiniLM-L6-v2".
- `device` (Literal["cpu", "cuda"], optional): Device to run the model on. Defaults to "cpu".

##### **`get_query_embedding(query: str) -> List[float]`**

Compute embedding for a query.

- `text` (str): Input query to compute embedding.

##### **`get_embedding_from_texts(texts: List[str]) -> List[List[float]]`**

Compute embeddings for a list of texts.

- `texts` (List[str])

##### **`get_documents_embedding(documents: List[str]) -> List[List[float]]`**

Compute embeddings for a list of Documents.

- `documents` (List[Documents])

## Ingestion: Directory Files

### Overview
This class provides functionality to load documents from a directory using various file loaders.

### API Reference

##### **`load_data(dir: str) -> List[Document]`**

Loads data from the specified directory.

- `dir` (str): The directory path from which to load the documents.
- `metadata` (Optional[dict]): Additional metadata to include in the document.

## Ingestion: IBM Cloud Object Store (s3)

### Overview
Loads data from IBM Cloud Object Storage (COS) using S3 interface.

### API Reference

##### **`IBMS3Loader(bucket: str, ibm_api_key_id: str, ibm_service_instance_id: str, s3_endpoint_url: str)`**

Initialize an IBMS3Loader object.

- `bucket` (str): The name of the IBM COS bucket.
- `ibm_api_key_id` (str): The IBM Cloud API key ID for accessing the bucket.
- `ibm_service_instance_id` (str): The service instance ID for the IBM COS.
- `s3_endpoint_url` (str): The endpoint URL for the IBM COS S3 service.

##### **`load_data() -> List[Document]`**

Loads data from the specified directory.

## Text Splitter: Semantic Splitter

### Overview
Semantic Splitter is a Python class designed to split text into chunks using semantic understanding. It utilizes pre-trained embeddings to identify breakpoints in the text and divide it into meaningful segments.

### API Reference

##### **`SemanticSplitter(model_name: str = "sentence-transformers/all-MiniLM-L6-v2", buffer_size: int = 1, breakpoint_threshold_amount: int = 95, device: Literal["cpu", "cuda"] = "cpu") -> None`**

Initialize the SemanticSplitter instance.

- `model_name`: Name of the pre-trained embeddings model to use. Default is "sentence-transformers/all-MiniLM-L6-v2".
- `buffer_size`: Size of the buffer for semantic chunking. Default is 1.
- `breakpoint_threshold_amount`: Threshold percentage for detecting breakpoints. Default is 95.
- `device`: Device to use for processing, either "cpu" or "cuda". Default is "cpu".

##### **`from_text(text: str) -> List[str]`**

Split text into chunks.
- `text`: Input text to split.

##### **`from_documents(documents: List[Document]) -> List[Document]`**

Split text from a list of documents into chunks.
- `documents`: List of Documents.

## Text Splitter: Sentence Splitter

### Overview
This Python class `SentenceSplitter` is designed to split input text into smaller chunks, particularly useful for processing large documents or texts. It provides methods to split text into chunks and to split a list of documents into chunks.

### API Reference

##### **`SentenceSplitter(chunk_size: int = 512, chunk_overlap: int = 256, length_function = len, separators: List[str] = ["\n\n", "\n", " ", ""]) -> None`**

Creates a new instance of the `SentenceSplitter` class.

- `chunk_size` (int, optional): Size of each chunk. Default is 512.
- `chunk_overlap` (int, optional): Amount of overlap between chunks. Default is 256.
- `length_function` (function, optional): Function to compute the length of the text. Default is `len`.
- `separators` (List[str], optional): List of separators used to split the text into chunks. Default separators are `["\n\n", "\n", " ", ""]`.


##### **`from_text(text: str) -> List[str]`**

Splits the input text into chunks.

- `text` (str): Input text to split.

##### **`from_documents(documents: List[Document]) -> List[Document]`**

Splits a list of documents into chunks.

- `documents` (List[Document]): List of Document objects.

## Vector Store: Elasticsearch

### Overview
The `ElasticsearchVectorStore` class provides functionality to interact with Elasticsearch for storing and querying document embeddings. It facilitates adding documents, performing similarity searches, and deleting documents from an Elasticsearch index.

### API Reference

##### **`ElasticsearchVectorStore(index_name, es_hostname, es_user, es_password, dims_length, embedding, batch_size=200, ssl=False, distance_strategy="cosine", text_field="text", vector_field="embedding")`**

Initializes the ElasticsearchVectorStore instance.

- `index_name`: The name of the Elasticsearch index.
- `es_hostname`: The hostname of the Elasticsearch instance.
- `es_user`: The username for authentication.
- `es_password`: The password for authentication.
- `dims_length`: The length of the embedding dimensions.
- `embedding`: An instance of embeddings.
- `batch_size`: The batch size for bulk operations. Defaults to 200.
- `ssl`: Whether to use SSL. Defaults to False.
- `distance_strategy`: The distance strategy for similarity search. Defaults to "cosine".
- `text_field`: The name of the field containing text. Defaults to "text".
- `vector_field`: The name of the field containing vector embeddings. Defaults to "embedding".

##### **`add_documents(documents, create_index_if_not_exists=True)`**

Adds documents to the Elasticsearch index.

- `documents`: A list of Document objects to add to the index.
- `create_index_if_not_exists`: Whether to create the index if it doesn't exist. Defaults to True.

##### **`similarity_search(query, top_k=4)`**

Performs a similarity search based on the documents most similar to the query.

- `query`: The query text.
- `top_k`: The number of top results to return. Defaults to 4.

##### **`delete(ids=None)`**

Deletes documents from the Elasticsearch index.

- `ids`: A list of document IDs to delete. Defaults to None.

