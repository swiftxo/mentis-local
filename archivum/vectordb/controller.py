from archivum.vectordb.client import get_chroma_client

def get_or_create_collection(storage_path: str, collection_name: str):
    client = get_chroma_client(storage_path)
    return client.get_or_create_collection(name=collection_name)

def list_collections(storage_path: str):
    client = get_chroma_client(storage_path)
    return client.list_collections()

def delete_collection(storage_path: str, collection_name: str):
    client = get_chroma_client(storage_path)
    client.delete_collection(name=collection_name)