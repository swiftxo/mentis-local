# Module: `query.py`

## Purpose
Handles retrieval of relevant document chunks from the `Archivum` vector database, either as plain text or with associated metadata.

---

## Functions

#### `retrieve_relevant_chunks`
- **Description**: Retrieves the top-N most relevant text chunks based on a user query.
- **Parameters**:  
  - `user_query` (str): The query string to search with.  
  - `n_results` (int, optional): Number of chunks to retrieve. Defaults to 5.
- **Returns**:  
  - `list[str]`: A list of retrieved text chunks.
- **Notes**:  
  - Verbose and debug logs provide detailed output if enabled in config.
  - Retrieves only the text content, not metadata or distance information.

---

#### `retrieve_chunks_with_metadata`
- **Description**: Retrieves the top-N relevant text chunks along with their metadata and similarity distance.
- **Parameters**:  
  - `user_query` (str): The query string to search with.  
  - `n_results` (int, optional): Number of chunks to retrieve. Defaults to 5.
- **Returns**:  
  - `list[dict]`: A list of dictionaries with keys `"text"`, `"metadata"`, and `"distance"`.
- **Notes**:  
  - Useful when you need more information than just the text (e.g., source file, page number, similarity score).
  - Verbose and debug logs available if enabled.

---

## Dependencies
- `archivum.db.Archivum`
- `archivum.config`
- `typing` (for list type hinting)

---

## Config Settings
- `config.VERBOSE`: Enables printing of high-level process logs.
- `config.DEBUG`: Enables detailed debugging information.
- `config.VECTOR_DB_PATH`: Path to the vector database directory.
- `config.COLLECTION_NAME`: Name of the collection within the vector database.

