import os
from tokenizers import Tokenizer, Encoding
from typing import Tuple, List


TOKENIZER_PATH = "assets/tokenizer.json"
PAD_ID = 1 
PAD_TOKEN = "<pad>"
MAX_LENGTH = 512

def load_tokenizer(path: str = TOKENIZER_PATH) -> Tokenizer:
    tokenizer = Tokenizer.from_file(path)
    tokenizer.enable_padding(length=MAX_LENGTH, pad_id=PAD_ID, pad_token=PAD_TOKEN)
    tokenizer.enable_truncation(max_length=MAX_LENGTH)
    return tokenizer


def tokenize(text: str, tokenizer: Tokenizer) -> Tuple[List[int], List[int]]:
    encoded = tokenizer.encode(text)
    return (encoded.ids, encoded.attention_mask)



def tokenize_raw(text: str, tokenizer: Tokenizer) -> Encoding:
    encoded = tokenizer.encode(text)
    return encoded
