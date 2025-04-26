
# Module: `chunker.py`

## Purpose
Provides functions to split text into manageable chunks using either a sliding window approach or a sentence-based token budget. Also includes utilities for debugging tokenization and chunking behavior.

---

## Functions

#### `sliding_window_chunk`
- **Description**: Chunks text into overlapping token-based windows.
- **Parameters**:  
  - `text` (str): Input text to chunk.  
  - `tokenizer` (`Tokenizer`): Pre-loaded tokenizer object.  
  - `window` (int, optional): Number of tokens per window. Defaults to `config.CHUNK_WINDOW`.  
  - `stride` (int, optional): Step size between window starts. Defaults to `config.CHUNK_STRIDE`.  
  - `min_tokens` (int, optional): Minimum number of tokens required to keep a chunk. Defaults to `config.CHUNK_MIN_TOKENS`.
- **Returns**:  
  - `List[str]`: List of decoded text chunks.
- **Notes**:  
  - Chunks overlap based on stride, useful for retaining context across segments.

---

#### `sentence_chunk`
- **Description**: Chunks text by grouping complete sentences without exceeding a maximum token limit.
- **Parameters**:  
  - `text` (str): Input text to chunk.  
  - `tokenizer` (`Tokenizer`): Pre-loaded tokenizer object.  
  - `max_tokens` (int, optional): Maximum tokens allowed per chunk. Defaults to `config.CHUNK_MAX_TOKENS`.  
  - `min_tokens` (int, optional): Minimum tokens required for a chunk to be kept. Defaults to `config.CHUNK_MIN_TOKENS`.
- **Returns**:  
  - `List[str]`: List of sentence-grouped text chunks.
- **Notes**:  
  - Prioritizes clean sentence boundaries while respecting token limits.

---

#### `chunk_text`
- **Description**: Hybrid chunking interface that dispatches between sentence-based or sliding window chunking based on the configured or given strategy.
- **Parameters**:  
  - `text` (str): Input text to chunk.  
  - `tokenizer` (`Tokenizer`): Pre-loaded tokenizer object.  
  - `strategy` (str, optional): Chunking strategy, `"sentence"` or `"sliding"`. Defaults to `config.CHUNK_METHOD`.  
  - `max_tokens` (int, optional): Max tokens for sentence chunking.  
  - `window` (int, optional): Window size for sliding window.  
  - `stride` (int, optional): Stride for sliding window.  
  - `min_tokens` (int, optional): Minimum tokens per chunk.  
  - `log` (bool, optional): Whether to print summary statistics. Defaults to `config.CHUNK_LOGGING`.
- **Returns**:  
  - `List[str]`: List of text chunks.
- **Notes**:  
  - Measures and logs chunking performance, including average tokens per chunk and total time taken.

---

#### `debug_token_chunk`
- **Description**: Debugging tool that decodes and displays a selected slice of token IDs from the input text.
- **Parameters**:  
  - `text` (str): Input text to tokenize.  
  - `tokenizer` (`Tokenizer`): Pre-loaded tokenizer object.  
  - `start` (int): Start index of the token slice.  
  - `end` (int): End index of the token slice.
- **Returns**:  
  - None
- **Notes**:  
  - Requires `config.DEBUG = True` to enable detailed debug output.

---

## Dependencies
- `time`
- `typing.List`
- `tokenizers`
- `nltk.tokenize.sent_tokenize`
- `archivum.tokenizer_utils.tokenize_raw`
- `archivum.config`

---

## Config Settings
- `config.VERBOSE`: Enables verbose chunking and summary logs.
- `config.DEBUG`: Enables detailed token visualization during debugging.
- `config.CHUNK_METHOD`: Default chunking method ("sentence" or "sliding").
- `config.CHUNK_MAX_TOKENS`: Max tokens per chunk (for sentence-based chunking).
- `config.CHUNK_WINDOW`: Token window size (for sliding window chunking).
- `config.CHUNK_STRIDE`: Step size for sliding window movement.
- `config.CHUNK_MIN_TOKENS`: Minimum valid chunk size.
- `config.CHUNK_LOGGING`: Enables additional chunking summary logs.
