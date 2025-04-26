import chromadb
from chromadb.api import ClientAPI

def get_chroma_client(storage_path: str) -> ClientAPI:
    return chromadb.PersistentClient(path=storage_path)
