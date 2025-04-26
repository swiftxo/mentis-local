import os
from tokenizers import Tokenizer, Encoding
from typing import Tuple, List
import archivum.config as config

VERBOSE = config.VERBOSE
DEBUG = config.DEBUG

def load_tokenizer(path: str = config.TOKENIZER_PATH) -> Tokenizer:
    """Load a tokenizer from file with padding/truncation enabled."""
    if VERBOSE:
        print(f"[Tokenizer|Load] Loading tokenizer from: {path}")

    tokenizer = Tokenizer.from_file(path)
    tokenizer.enable_padding(length=config.TOKENIZER_MAX_LENGTH, pad_id=config.TOKENIZER_PAD_ID, pad_token=config.TOKENIZER_PAD_TOKEN)
    tokenizer.enable_truncation(max_length=config.TOKENIZER_MAX_LENGTH)

    if VERBOSE:
        print(f"[Tokenizer|Load] Tokenizer loaded. Padding to {config.TOKENIZER_MAX_LENGTH} tokens.")

    return tokenizer

def tokenize(text: str, tokenizer: Tokenizer) -> Tuple[List[int], List[int]]:
    """Tokenize text into (ids, attention_mask)."""
    if DEBUG:
        print(f"[Tokenizer|Tokenize] Encoding text: {text[:50]}...")

    encoded = tokenizer.encode(text)

    if DEBUG:
        print(f"[Tokenizer|Tokenize] Token IDs: {encoded.ids}")
        print(f"[Tokenizer|Tokenize] Attention Mask: {encoded.attention_mask}")

    return (encoded.ids, encoded.attention_mask)

def tokenize_raw(text: str, tokenizer: Tokenizer) -> Encoding:
    """Tokenize text and return raw Encoding object."""
    if DEBUG:
        print(f"[Tokenizer|TokenizeRaw] Encoding text: {text[:50]}...")

    encoded = tokenizer.encode(text)

    if DEBUG:
        print(f"[Tokenizer|TokenizeRaw] Raw Encoding: IDs = {encoded.ids}")

    return encoded
