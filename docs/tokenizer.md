# `tokenizer_utils.py`: Tokenization Utilities

This module handles text-to-token conversion using a custom Hugging Face-compatible tokenizer (`tokenizer.json`). It supports truncation and padding for consistent input lengths.

Tokenization is required before:
- Chunking (to enforce token budgets)
- Embedding (for token-aware models or stats)
- LLM input formatting

## Constants

<details>
<summary>Defaults:</summary>

- `TOKENIZER_PATH`: `"assets/tokenizer.json"`  
- `PAD_ID`: `1`  
- `PAD_TOKEN`: `"<pad>"`  
- `MAX_LENGTH`: `512`
</details>



## `load_tokenizer(path=TOKENIZER_PATH)`

Loads a tokenizer from disk and enables:
- Padding to a fixed `MAX_LENGTH`
- Truncation beyond `MAX_LENGTH`

Returns: Initialized `Tokenizer` instance



## `tokenize(text, tokenizer)`

Encodes a single text into:
- `token_ids` (List[int])
- `attention_mask` (List[int])

Returns: `(token_ids, attention_mask)`



## `tokenize_raw(text, tokenizer)`

Returns the full `Encoding` object for more detailed access (e.g. offsets, tokens, etc).

Returns: `Encoding` (from Hugging Face `tokenizers`)



## Usage

This module standardizes input length and encoding behavior across:
- Chunking pipelines (token-aware slicing)
- Debugging tools (`debug_token_chunk`)
- LLM input construction and analysis