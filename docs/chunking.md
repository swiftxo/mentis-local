# `chunker.py`: Text Chunking Strategies

This module provides two chunking strategies to split raw text into smaller segments that fit within a token budget. These chunks are optimized for embedding and retrieval.

The two main approaches are:
- Sentence-based chunking (preserves semantic boundaries)
- Sliding window chunking (preserves fixed-length token context)

Both methods aim to produce high-quality, token-length-constrained chunks of text.

## `sliding_window_chunk(text, tokenizer, window=150, stride=30, min_tokens=10)`

Chunks text using overlapping token windows.

<details>
<summary>Process:</summary>

- Tokenizes the input text
- Slides a fixed-size window (`window`) over the tokens with a specified `stride`
- Discards chunks with fewer than `min_tokens`
- Decodes each token window into a string
</details>

Returns: `List[str]` of decoded overlapping text chunks

## `sentence_chunk(text, tokenizer, max_tokens=512, min_tokens=10)`

Groups full sentences into chunks that stay within a max token budget.

<details>
<summary>Process:</summary>

- Splits text into sentences using `nltk.sent_tokenize`
- Accumulates sentences until token count exceeds `max_tokens`
- Discards under-sized chunks (less than `min_tokens`)
</details>

Returns: `List[str]` of semantically coherent text chunks

## `chunk_text(text, tokenizer, strategy="sentence", ...)`

Unified interface for both chunking strategies.

<details>
<summary>Parameters:</summary>

- `strategy` (str): `"sentence"` or `"sliding"`
- `max_tokens`, `window`, `stride`, `min_tokens`: chunking parameters
- `log` (bool): If `True`, prints chunking stats
</details>

Returns: `List[str]` of chunked text

## `debug_token_chunk(text, tokenizer, start, end)`

Utility to visualize a token slice.

<details>
<summary>Outputs:</summary>

- Raw token IDs from `start` to `end`
- Decoded text segment for inspection
</details>

Returns: `None` (prints output for debugging)

## Usage

This module is used during preprocessing to:
- Ensure chunks are LLM-friendly (under token limits)
- Control chunk size and overlap
- Maintain context relevance in retrieval

You can choose between semantic (`sentence`) or mechanical (`sliding`) strategies depending on your use case.