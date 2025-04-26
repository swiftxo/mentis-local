# Module: `document.py`

## Purpose
Defines core data structures for representing parsed documents and their text chunks, along with helper methods for easy manipulation and serialization.

---

## Classes

#### `DocumentChunk`
- **Description**: Represents a chunk of text along with its associated metadata.
- **Attributes**:  
  - `text` (str): The text content of the chunk.  
  - `metadata` (dict): Metadata associated with the chunk (e.g., page number, file path).
- **Methods**:  
  - `__repr__()`: Returns a shortened preview of the chunk for easier debugging.  
  - `__len__()`: Returns the character length of the chunk text.  
  - `get_metadata()`: Returns the metadata dictionary.  
  - `to_dict()`: Serializes the chunk into a dictionary format.
- **Notes**:  
  - If no metadata is provided, an empty dictionary is assigned by default.

---

#### `Document`
- **Description**: Represents a full document made up of multiple `DocumentChunk` objects.
- **Attributes**:  
  - `chunks` (list[DocumentChunk]): List of text chunks that compose the document.
- **Methods**:  
  - `__repr__()`: Returns a summary showing the number of chunks.  
  - `__len__()`: Returns the number of chunks in the document.  
  - `get_chunks()`: Retrieves the list of chunks.  
  - `to_dict()`: Serializes the document into a list of chunk dictionaries.
- **Notes**:  
  - Treats a document as simply a collection of its chunks, without enforcing structure beyond that.

---

## Dependencies
- None (standard Python only)

---

## Config Settings
- None