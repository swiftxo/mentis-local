# Module: `parser.py`

## Purpose
Parses different file types (PDF, Markdown, Text) into `Document` objects containing `DocumentChunks` with associated text and metadata. Provides utilities to parse single files or entire folders.

---

## Functions

#### `parse_pdf`
- **Description**: Parses a PDF file and returns a `Document` with one chunk per page containing text and metadata.
- **Parameters**:  
  - `file_path` (str): Path to the PDF file.
- **Returns**:  
  - `Document`: A document object containing all text chunks from the PDF.
- **Notes**:  
  - Only extracts plain text from each page (no images or structured formatting).

---

#### `parse_md`
- **Description**: Parses a Markdown file into a single `DocumentChunk`.
- **Parameters**:  
  - `file_path` (str): Path to the Markdown file.
- **Returns**:  
  - `Document`: A document object containing one chunk with the full Markdown text.
- **Notes**:  
  - Treats the entire Markdown file as a single chunk.

---

#### `parse_txt`
- **Description**: Parses a plain text file into a single `DocumentChunk`.
- **Parameters**:  
  - `file_path` (str): Path to the text file.
- **Returns**:  
  - `Document`: A document object containing one chunk with the full text content.
- **Notes**:  
  - Treats the entire text file as a single chunk.

---

#### `parse_file`
- **Description**: Dispatches parsing based on file extension (.pdf, .md, .txt).
- **Parameters**:  
  - `file_path` (str): Path to the file.
- **Returns**:  
  - `Document`: A parsed document object appropriate to the file type.
- **Notes**:  
  - Raises `ValueError` if an unsupported file type is provided.

---

#### `parse_folder`
- **Description**: Parses all supported files in a folder recursively into a list of `Document` objects.
- **Parameters**:  
  - `folder_path` (str): Path to the folder.
- **Returns**:  
  - `list[Document]`: A list of parsed document objects.
- **Notes**:  
  - Supported file types: `.pdf`, `.md`, `.txt`
  - Recursively searches subfolders.

---

## Dependencies
- `pymupdf`
- `json`
- `pathlib.Path`
- `archivum.document.Document`
- `archivum.document.DocumentChunk`
- `archivum.config`

---

## Config Settings
- `config.VERBOSE`: Enables printing detailed process logs.
- `config.DEBUG`: Enables detailed debugging output.
  
