from sentence_transformers import SentenceTransformer
from typing import List
import torch
import archivum.config as config

VERBOSE = config.VERBOSE
DEBUG = config.DEBUG

def load_embedder(model_name: str = config.EMBED_MODEL_NAME) -> SentenceTransformer:
    """Load a sentence embedding model with device auto-detection."""
    
    if config.EMBED_DEVICE == "auto":
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    else:
        device = config.EMBED_DEVICE

    if VERBOSE:
        print(f"[Embedder|Load] Loading embedder model: {model_name} on device: {device}")

    model = SentenceTransformer(model_name, device=device)

    if VERBOSE:
        print(f"[Embedder|Load] Model loaded successfully.")

    return model

def embed_texts(texts: List[str],model: SentenceTransformer,normalize: bool = config.EMBED_NORMALIZE,
                as_tensor: bool = config.EMBED_AS_TENSOR,batch_size: int = config.EMBED_BATCH_SIZE) -> torch.Tensor:
    """Embed a list of texts using E5 with optional normalization and batching."""
    
    if VERBOSE:
        print(f"[Embedder|Embed] Embedding {len(texts)} texts... Batch size: {batch_size} | Normalize: {normalize} | Tensor Output: {as_tensor}")

    embeddings = model.encode(
        texts,
        batch_size=batch_size,   
        convert_to_tensor=as_tensor,
        normalize_embeddings=normalize,
    )

    if DEBUG:
        if isinstance(embeddings, torch.Tensor):
            sample_vector = embeddings[0][:5].tolist()
        else:
            sample_vector = embeddings[0][:5]
        print(f"[Embedder|Debug] Sample embedding: {sample_vector}")

    return embeddings

def get_detailed_instruct(task_description: str, query: str) -> str:
    """Format a detailed instruction for embedding input."""
    detailed = f"Instruct: {task_description}\nQuery: {query}"

    if DEBUG:
        print(f"[Embedder|Debug] Detailed instruct created:\n{detailed}")

    return detailed
