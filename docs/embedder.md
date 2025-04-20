# `embedder.py`: Embedding Utilities

This module handles the transformation of chunked text into vector embeddings using the `intfloat/multilingual-e5-large-instruct` model via `sentence-transformers`.

The output vectors are used to:
- Store chunks in a vector database (e.g., ChromaDB)
- Compare similarity between queries and stored chunks
- Enable fast and semantically aware retrieval

## `load_embedder(model_name=...)`

Loads the E5 embedding model from Hugging Face via `SentenceTransformer`.

<details>
<summary>Defaults:</summary>

- `model_name`: `"intfloat/multilingual-e5-large-instruct"`
</details>

Returns: `SentenceTransformer` model instance

## `embed_texts(texts, model, normalize=True, as_tensor=True)`

Embeds a list of input texts into dense vectors.

<details>
<summary>Parameters:</summary>

- `texts` (List[str]): Input texts or chunks
- `model` (SentenceTransformer): Loaded E5 model
- `normalize` (bool): Normalize output vectors to unit length
- `as_tensor` (bool): Return as a `torch.Tensor` if `True`
</details>

Returns: `torch.Tensor` or `List[np.ndarray]` of vector embeddings

## `get_detailed_instruct(task_description, query)`

Formats a query using E5's expected input format for instruction-following tasks.

<details>
<summary>Format:</summary>

``` 
Instruct: {task_description}
Query: {query}
```
</details>

Returns: Formatted string to be embedded

## Usage

This module is called after chunking. It converts structured text chunks or search queries into vector form, enabling similarity search and LLM-enhanced reasoning steps.