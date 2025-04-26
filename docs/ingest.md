
# Module: `ingest.py`

## Purpose
Handles the ingestion pipeline: parses new documents, chunks their text, embeds the chunks, and stores them into the vector database. Tracks already-ingested files to avoid duplicates.

---

## Functions

#### `load_ingested_files`
- **Description**: Loads the set of file paths that have already been ingested.
- **Parameters**:  
  - None
- **Returns**:  
  - `set`: A set containing previously ingested file paths.
- **Notes**:  
  - If the tracker file does not exist, returns an empty set.

---

#### `save_ingested_files`
- **Description**: Saves the updated set of ingested file paths to the tracker file.
- **Parameters**:  
  - `files` (set): Set of ingested file paths to save.
- **Returns**:  
  - None
- **Notes**:  
  - Saves the set as a JSON array for persistence across runs.

---

#### `ingest`
- **Description**: Runs the ingestion pipeline: parses new files, chunks their content, embeds them, and adds them to the vector database.
- **Parameters**:  
  - `path` (str, optional): Path to the folder to ingest from. Defaults to `config.DATA_FOLDER`.
- **Returns**:  
  - None
- **Notes**:  
  - Only ingests new files that have not been seen before.
  - Files supported: `.pdf`, `.md`, `.txt`
  - Verbose logging provides detailed progress output if enabled.

---

## Dependencies
- `archivum.config`
- `archivum.parser.parse_file`
- `archivum.tokenizer_utils.load_tokenizer`
- `archivum.chunker.chunk_text`
- `archivum.db.Archivum`
- `json`
- `pathlib.Path`

---

## Config Settings
- `config.VERBOSE`: Enables detailed output during ingestion.
- `config.DATA_FOLDER`: The root folder to search for documents.
- `config.VECTOR_DB_PATH`: Path to the vector database storage.
- `config.COLLECTION_NAME`: Name of the collection to store ingested chunks.

