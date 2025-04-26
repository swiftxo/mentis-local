

# Module: `vectordb (client.py + controller.py)`

## Purpose
Provides a thin wrapper around ChromaDB’s `PersistentClient` to simplify database client management, collection creation, listing, and deletion.

---

## Functions

#### `get_chroma_client`
- **Location**: `client.py`
- **Description**: Initializes and returns a ChromaDB persistent client at the given storage path.
- **Parameters**:  
  - `storage_path` (str): Filesystem path to the ChromaDB database folder.
- **Returns**:  
  - `ClientAPI`: A connected `PersistentClient` instance.
- **Notes**:  
  - Used internally by collection management functions.

---

#### `get_or_create_collection`
- **Location**: `controller.py`
- **Description**: Connects to the ChromaDB client and retrieves an existing collection or creates a new one if it doesn't exist.
- **Parameters**:  
  - `storage_path` (str): Filesystem path to the ChromaDB database folder.  
  - `collection_name` (str): Name of the collection to retrieve or create.
- **Returns**:  
  - `Collection`: A ChromaDB collection object ready for use.

---

#### `list_collections`
- **Location**: `controller.py`
- **Description**: Lists all available collections under the given storage path.
- **Parameters**:  
  - `storage_path` (str): Filesystem path to the ChromaDB database folder.
- **Returns**:  
  - `list`: List of available collection names.
- **Notes**:  
  - Useful for debugging or verifying existing collections.

---

#### `delete_collection`
- **Location**: `controller.py`
- **Description**: Deletes a specific collection from the ChromaDB storage.
- **Parameters**:  
  - `storage_path` (str): Filesystem path to the ChromaDB database folder.  
  - `collection_name` (str): Name of the collection to delete.
- **Returns**:  
  - None
- **Notes**:  
  - Fully deletes the specified collection from storage.

---

## Dependencies
- `chromadb`
- `chromadb.api.ClientAPI`

---

## Config Settings
- None (storage paths are passed explicitly)


