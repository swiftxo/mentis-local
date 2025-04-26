from archivum.db import Archivum
import archivum.config as config

VERBOSE = config.VERBOSE
DEBUG = config.DEBUG

db = Archivum(storage_path=config.VECTOR_DB_PATH, collection_name=config.COLLECTION_NAME)

def retrieve_relevant_chunks(user_query: str, n_results: int = 5) -> list[str]:
    """
    Retrieve top-n relevant chunks for a given user query.
    """
    if VERBOSE:
        print(f"[Query|Retrieve] Retrieving top {n_results} chunks for query: '{user_query}'")

    # Query Archivum
    results = db.query(query_text=user_query, n_results=n_results)

    retrieved_chunks = results.get("documents", [[]])[0]  # because ChromaDB returns list-of-lists

    if VERBOSE:
        print(f"[Query|Retrieve] Retrieved {len(retrieved_chunks)} chunks.")

    if DEBUG:
        for idx, chunk in enumerate(retrieved_chunks, 1):
            print(f"[Query|Debug] Chunk {idx}: {chunk[:100]}...")

    return retrieved_chunks

def retrieve_chunks_with_metadata(user_query: str, n_results: int = 5) -> list[dict]:
    """
    Retrieve top-n relevant chunks along with their metadata.
    """
    if VERBOSE:
        print(f"[Query|Retrieve+Meta] Retrieving top {n_results} chunks + metadata for query: '{user_query}'")

    results = db.query(query_text=user_query, n_results=n_results)

    # Combine chunks, metadata, distances into a friendly list
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    combined = []
    for doc, meta, dist in zip(documents, metadatas, distances):
        combined.append({
            "text": doc,
            "metadata": meta,
            "distance": dist
        })

    if VERBOSE:
        print(f"[Query|Retrieve+Meta] Retrieved {len(combined)} chunks with metadata.")

    if DEBUG:
        for idx, item in enumerate(combined, 1):
            print(f"[Query|Debug] Chunk {idx}: Distance={item['distance']:.4f}, Metadata={item['metadata']}")

    return combined
