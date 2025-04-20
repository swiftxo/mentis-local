# `document.py`: Core Data Structures

This module defines two classes used across the pipeline to represent parsed and chunked content.

The parser modules output a `Document`, composed of `DocumentChunk`s. These are passed into:
- The chunker (if further chunking is needed)
- The embedder (for vectorization)
- The retriever (for similarity search)

They act as a **lightweight memory unit** for the system.


## `class DocumentChunk`

A small unit of text (usually a sentence or paragraph) paired with metadata. This is the **core unit** that gets embedded and stored in the vector database.

<details>
<summary>Attributes:</summary>

- `text` (str): The chunked text.
- `metadata` (dict): Optional metadata like page number, source file, etc.
</details>

<details>
<summary>Methods:</summary>

- `__repr__()` → Short preview for debugging.
- `__len__()` → Returns length of the text.
- `get_metadata()` → Access metadata.
- `to_dict()` → Serialize chunk for storage.
</details>


## `class Document`

Wraps a list of `DocumentChunk` objects. Represents a fully parsed file.

<details>
<summary>Attributes:</summary>

- `chunks` (list[DocumentChunk]): All chunks from a single document.
</details>

<details>
<summary>Methods:</summary>

- `__repr__()` → Summary of number of chunks.
- `__len__()` → Returns number of chunks.
- `get_chunks()` → Access underlying chunks.
- `to_dict()` → Serialize the document as a list of dicts.
</details>