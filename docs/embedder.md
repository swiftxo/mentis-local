# Module: `embedder.py`

## Purpose
Handles loading of the sentence embedding model and provides utilities for embedding text batches with configurable normalization and output format. Also provides a helper for formatting detailed instruction prompts.


## Functions

#### `load_embedder`
- **Description**: Loads a sentence embedding model with automatic device detection (CPU or GPU).
- **Parameters**:  
  - `model_name` (str, optional): Name or path of the model to load. Defaults to `config.EMBED_MODEL_NAME`.
- **Returns**:  
  - `SentenceTransformer`: A loaded embedding model.
- **Notes**:  
  - Device selection respects `config.EMBED_DEVICE` or defaults to auto-detecting GPU if available.

---

#### `embed_texts`
- **Description**: Embeds a list of text inputs into dense vectors, with optional normalization and batching.
- **Parameters**:  
  - `texts` (List[str]): List of input text strings to embed.  
  - `model` (`SentenceTransformer`): Pre-loaded sentence embedding model.  
  - `normalize` (bool, optional): Whether to normalize embeddings. Defaults to `config.EMBED_NORMALIZE`.  
  - `as_tensor` (bool, optional): Whether to return results as a PyTorch tensor. Defaults to `config.EMBED_AS_TENSOR`.  
  - `batch_size` (int, optional): Number of texts per batch during encoding. Defaults to `config.EMBED_BATCH_SIZE`.
- **Returns**:  
  - `torch.Tensor` or `List[List[float]]`: Batch of embeddings.
- **Notes**:  
  - Supports GPU acceleration if available.

---

#### `get_detailed_instruct`
- **Description**: Formats a task description and user query into a detailed instruction prompt for models that use instruction-based embeddings.
- **Parameters**:  
  - `task_description` (str): Description of the task for context.  
  - `query` (str): The specific query or input.
- **Returns**:  
  - `str`: A formatted string combining the task and query.
- **Notes**:  
  - Mainly useful if using instruction-tuned models like E5 variants.


## Dependencies
- `sentence_transformers`
- `torch`
- `typing` (`List`)
- `archivum.config`

---

## Config Settings
- `config.VERBOSE`: Enables verbose output during model loading and embedding.
- `config.DEBUG`: Enables detailed debug outputs (sample embeddings, instructions).
- `config.EMBED_MODEL_NAME`: Default model name to load.
- `config.EMBED_DEVICE`: Preferred device for inference ("cpu", "cuda", or "auto").
- `config.EMBED_NORMALIZE`: Whether embeddings should be L2-normalized.
- `config.EMBED_AS_TENSOR`: Whether output should be a PyTorch tensor.
- `config.EMBED_BATCH_SIZE`: Number of samples to process in one batch during encoding.
