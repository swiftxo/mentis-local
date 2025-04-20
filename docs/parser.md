# `parser.py`: File Parsing Utilities

This module converts raw input files (`.pdf`, `.md`, `.txt`) into a standardized `Document` object composed of `DocumentChunk`s.

These parsed documents are then passed into:
- The chunker (for token-aware splitting)
- The embedder (for generating embeddings)
- The vector DB (for storage + retrieval)

It acts as the **entry point for data ingestion** into the `mentis-local` system.



## `parse_pdf(file_path)`

Parses a PDF file page-by-page using `PyMuPDF`, extracting text and storing each page as a separate `DocumentChunk`.

<details>
<summary>Process:</summary>

- Iterate over each page
- Extract text via `get_text("text")`
- Create a `DocumentChunk` per non-empty page
- Attach `page_number`, `file_path`, and `file_type` as metadata
</details>

**Returns:** `Document` object with one chunk per page


## `parse_md(file_path)`

Parses a Markdown file as a single `DocumentChunk`.

<details>
<summary>Process:</summary>

- Read the entire `.md` file as raw text
- Strip leading/trailing whitespace
- Wrap in one `DocumentChunk` with `file_path` and `file_type` metadata
</details>

**Returns:** `Document` object with a single chunk



## `parse_txt(file_path)`

Identical to `parse_md`, but for plain `.txt` files.

<details>
<summary>Process:</summary>

- Read entire `.txt` file
- Strip whitespace
- Create one `DocumentChunk` with basic metadata
</details>

**Returns:** `Document` object with a single chunk



## `parse_file(file_path)`

High-level parser that dispatches to the appropriate function based on file extension.

<details>
<summary>Supported Extensions:</summary>

- `.pdf` → `parse_pdf`
- `.md` → `parse_md`
- `.txt` → `parse_txt`
</details>

**Raises:** `ValueError` if an unsupported file extension is passed.



## Example Output

```python
< Document with 3 chunks >

DocumentChunk(
    text='Canada’s productivity challenge is not...', 
    metadata={
        'page_number': 1, 
        'file_path': 'docs/budget.pdf', 
        'file_type': 'pdf'
    }
)
```