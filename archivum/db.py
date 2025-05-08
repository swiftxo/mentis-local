from archivum.vectordb.controller import get_or_create_collection, delete_collection
from archivum.embedder import load_embedder, embed_texts, get_detailed_instruct
import archivum.config as config
from pathlib import Path
import json

VERBOSE = config.VERBOSE
DEBUG = config.DEBUG
class Archivum:

    def __init__(self, storage_path: str, collection_name: str):
        """Initialize the Archivum with a storage path and collection name."""
        self.storage_path = storage_path
        self.collection_name = collection_name
        self.collection = get_or_create_collection(storage_path, collection_name)
        self.embedder = load_embedder()
        self.tracker_path = Path(storage_path) / f"{collection_name}_ingested_files.json"


        if VERBOSE:
            print(f"[Archivum|Init] Connected to collection '{self.collection_name}' at '{self.storage_path}'.")


    def load_ingested_files(self) -> set:
        """Load the set of already-ingested file paths."""
        if not self.tracker_path.exists():
            return set()
        with open(self.tracker_path, "r") as f:
            return set(json.load(f))
        
    def save_ingested_files(self, files: set):
        """Save the updated set of ingested file paths."""
        with open(self.tracker_path, "w") as f:
            json.dump(list(files), f, indent=2)

        

    def add_documents(self, documents: list[str], ids: list[str], metadatas: list[dict] = None):
        """Add documents to the Archivum, embedding them first."""

        if VERBOSE:
            print(f"[Archivum|Add] Embedding {len(documents)} documents...")

        embeddings = embed_texts(documents, model=self.embedder, normalize=True, as_tensor=False)
        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )

        if VERBOSE:
            print(f"[Archivum|Add] Added {len(documents)} documents to collection '{self.collection_name}'.")
        
    def delete_documents(self, ids: list[str]):
        """Delete documents from the Archivum by their IDs."""
        if VERBOSE:
            print(f"[Archivum|Delete] Deleting {len(ids)} documents...")

        self.collection.delete(ids=ids)

        if VERBOSE:
            print(f"[Archivum|Delete] Deleted {len(ids)} documents from collection '{self.collection_name}'.")

    def list_documents(self):
        """List all documents' IDs currently in the Archivum."""
        ids = self.collection.get(ids=None)["ids"]

        if VERBOSE:
            print(f"[Archivum|List] Found {len(ids)} documents in collection '{self.collection_name}'.")

        if DEBUG:
            print(f"[Archivum|List] Document IDs: {ids}")

        return ids

    def reset_collection(self):
        """Completely wipe and recreate the collection."""
        if VERBOSE:
            print(f"[Archivum|Reset] Resetting collection '{self.collection_name}'...")

        delete_collection(self.storage_path, self.collection_name)
        self.collection = get_or_create_collection(self.storage_path, self.collection_name)

        if VERBOSE:
            print(f"[Archivum|Reset] Collection '{self.collection_name}' reset complete.")

    def query(self, query_text: str, n_results: int = 5, task_description: str = "Retrieve relevant passages for the query"):
        """
        Query the Archivum for documents similar to the query text.
        """
        if VERBOSE:
            print(f"[Archivum|Query] Querying for: '{query_text}' | Top {n_results} results")

        # Format the query using the instruction format for E5 models
        instructed_query = get_detailed_instruct(task_description, query_text) 
        
        # Embed the instructed query
        query_embedding = embed_texts(
            [instructed_query], 
            model=self.embedder, 
            normalize=True, 
            as_tensor=False 
        )

        # Perform the query using the ChromaDB collection's query method
        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=n_results,
            include=['metadatas', 'documents', 'distances']
        )

        if VERBOSE:
            print(f"[Archivum|Query] Retrieved {len(results.get('documents', [[]])[0])} chunks.")

        if DEBUG:
            print(f"[Archivum|Query|DEBUG] Full results structure: {results}")

        return results