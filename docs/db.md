
# Module: `db.py`

## Purpose
Defines the `Archivum` class, which manages interactions with the vector database: adding, deleting, listing, resetting documents, and querying based on embedded text.

---

## Classes

#### `Archivum`
- **Description**: Main interface for storing, retrieving, and managing document embeddings in a ChromaDB-backed vector database.
- **Attributes**:  
  - `storage_path` (str): Path to the database storage location.  
  - `collection_name` (str): Name of the collection inside the database.  
  - `collection`: Reference to the active ChromaDB collection object.  
  - `embedder`: Loaded sentence embedding model.
- **Methods**:
  
  - `__init__(storage_path: str, collection_name: str)`  
    - Initializes Archivum by connecting to or creating a collection, and loading the embedding model.
  
  - `add_documents(documents: list[str], ids: list[str], metadatas: list[dict] = None)`  
    - Embeds and adds documents with corresponding IDs and optional metadata.

  - `delete_documents(ids: list[str])`  
    - Deletes documents from the collection by their IDs.

  - `list_documents()`  
    - Lists all document IDs currently stored in the collection.

  - `reset_collection()`  
    - Completely deletes and recreates the collection.

  - `query(query_text: str, n_results: int = 5, task_description: str = "Retrieve relevant passages for the query")`  
    - Embeds the query and retrieves the top-N most similar documents, along with metadata and distances.

- **Notes**:  
  - Verbose and debug logs available at all major steps for traceability.
  - Querying uses a task-instruction format optimized for models like E5.

---

## Dependencies
- `archivum.vectordb.controller.get_or_create_collection`
- `archivum.vectordb.controller.delete_collection`
- `archivum.embedder.load_embedder`
- `archivum.embedder.embed_texts`
- `archivum.embedder.get_detailed_instruct`
- `archivum.config`

---

## Config Settings
- `config.VERBOSE`: Enables detailed high-level process logging.
- `config.DEBUG`: Enables detailed debug outputs (e.g., full query results).
- (Indirectly depends on `config` settings used by `embedder` too, e.g., device selection, normalization.)
