import time
from typing import List
from tokenizers import Tokenizer
from nltk.tokenize import sent_tokenize
from .tokenizer_utils import tokenize_raw
import nltk
nltk.download('punkt_tab')


def sliding_window_chunk(text: str, tokenizer: Tokenizer, window: int = 150, stride: int = 30, min_tokens: int = 10) -> List[str]:
    """Chunk text into overlapping token windows."""

    enc = tokenize_raw(text, tokenizer)
    ids = enc.ids
    chunks = []

    for i in range(0, len(ids), stride):
        window_ids = ids[i:i + window]

        if len(window_ids) < min_tokens:
            continue
        
        chunk = tokenizer.decode(window_ids, skip_special_tokens=True)
        chunks.append(chunk)

    return chunks


def sentence_chunk(text: str, tokenizer: Tokenizer, max_tokens: int = 512, min_tokens: int = 10) -> List[str]:
    """Chunk text by grouping whole sentences under a token budget."""
    
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    current_len = 0

    for sent in sentences:
        enc = tokenize_raw(sent, tokenizer)
        sent_len = len(enc.ids)
        if current_len + sent_len <= max_tokens:
            current_chunk += " " + sent
            current_len += sent_len
        else:
            if current_len >= min_tokens:
                chunks.append(current_chunk.strip())
            current_chunk = sent
            current_len = sent_len

    if current_chunk and current_len >= min_tokens:
        chunks.append(current_chunk.strip())

    return chunks


def chunk_text(text: str,tokenizer: Tokenizer,strategy: str = "sentence",max_tokens: int = 512,
               window: int = 150,stride: int = 30,min_tokens: int = 10,log: bool = False) -> List[str]:
    """Hybrid chunking interface supporting both sentence and sliding strategies."""

    start = time.perf_counter()
    if strategy == "sentence":
        chunks = sentence_chunk(text, tokenizer, max_tokens=max_tokens, min_tokens=min_tokens)
    elif strategy == "sliding":
        chunks = sliding_window_chunk(text, tokenizer, window=window, stride=stride, min_tokens=min_tokens)
    else:
        raise ValueError(f"Unknown chunking strategy: {strategy}")
    end = time.perf_counter()

    if log:
        token_count = len(tokenize_raw(text, tokenizer).ids)
        print(f"[Chunking] Strategy: {strategy} | Tokens: {token_count} | Chunks: {len(chunks)} | Avg tokens/chunk: {round(token_count/len(chunks), 1)} | Time: {round(end-start, 4)}s")

    return chunks


def debug_token_chunk(text: str, tokenizer, start: int, end: int):
    enc = tokenizer.encode(text)
    slice_ids = enc.ids[start:end]
    decoded = tokenizer.decode(slice_ids, skip_special_tokens=True)
    print(f"Tokens {start}:{end} →", slice_ids)
    print("Decoded Text →", decoded)