from sentence_transformers import SentenceTransformer
from typing import List
import torch

MODEL_NAME = "intfloat/multilingual-e5-large-instruct"

def load_embedder(model_name: str = MODEL_NAME) -> SentenceTransformer:
    return SentenceTransformer(model_name)

def embed_texts(texts: List[str], model: SentenceTransformer, normalize: bool = True, as_tensor: bool = True) -> torch.Tensor:
    """Embed a list of texts using E5 with optional normalization."""
    return model.encode(
        texts,
        convert_to_tensor=as_tensor,
        normalize_embeddings=normalize,
    )

def get_detailed_instruct(task_description: str, query: str) -> str:
    return f"Instruct: {task_description}\nQuery: {query}"
