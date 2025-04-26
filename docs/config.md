
# Module: `config.py`

## Purpose
Centralized configuration file that defines all key settings for the Archivum system, including paths, model parameters, chunking behavior, and verbosity levels.

---

## Configuration Categories

#### Vectorstore / Database Settings
- **`VECTOR_DB_PATH`** (str): Path where ChromaDB collections are stored.
- **`COLLECTION_NAME`** (str): Default name of the collection to create or use.
- **`DATA_FOLDER`** (str): Folder path containing files to ingest into the database.

---

#### Embedding Settings
- **`EMBED_MODEL_NAME`** (str): Name of the embedding model to load (e.g., multilingual E5 model).
- **`EMBED_BATCH_SIZE`** (int): Number of texts processed per batch during embedding.
- **`EMBED_NORMALIZE`** (bool): Whether to normalize output embeddings to unit length.
- **`EMBED_AS_TENSOR`** (bool): Whether to output embeddings as PyTorch tensors (True) or numpy arrays (False).
- **`EMBED_DEVICE`** (str): Device selection — "auto" (GPU if available), or force "cuda"/"cpu".
- **`EMBED_TIMEOUT`** (int): Maximum seconds to wait per batch operation (rarely needed).

---

#### Chunking Settings
- **`CHUNK_METHOD`** (str): Chunking strategy — options: `"sentence"` or `"sliding_window"`.
- **`CHUNK_MAX_TOKENS`** (int): Maximum number of tokens allowed per chunk.
- **`CHUNK_WINDOW`** (int): Window size for sliding window chunking.
- **`CHUNK_STRIDE`** (int): Stride (step size) for moving the sliding window.
- **`CHUNK_MIN_TOKENS`** (int): Minimum number of tokens a chunk must have to be kept.
- **`CHUNK_LOGGING`** (bool): Whether to log debug information during chunking.

---

#### Tokenizer Settings
- **`TOKENIZER_PATH`** (str): Path to the tokenizer JSON file.
- **`TOKENIZER_PAD_ID`** (int): Token ID used for padding operations.
- **`TOKENIZER_PAD_TOKEN`** (str): Token string used for padding.
- **`TOKENIZER_MAX_LENGTH`** (int): Maximum input length for padding/truncation.

---

#### General Settings
- **`VERBOSE`** (bool): Enables general verbose logging across modules.
- **`DEBUG`** (bool): Enables detailed debug output across modules.

---

## Dependencies
- None (pure static configuration)

---

## Notes
- All other modules (`db.py`, `embedder.py`, `tokenizer_utils.py`, etc.) read from this config file to remain centralized and easily adjustable.
- Changing settings here allows tuning the system without touching the code logic.
