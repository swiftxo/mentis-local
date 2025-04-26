
# 📚 Archivum Documentation

Welcome to the internal documentation for **Archivum Mentis** — a modular, local-first knowledge assistant.

This documentation covers every major module and how they fit together.

---

## 📄 Modules

- [`config.py`](config.md)  
  Centralized system settings for embedding, tokenization, chunking, and database management.

- [`document.py`](document.md)  
  Defines `Document` and `DocumentChunk` classes to represent parsed text data.

- [`tokenizer_utils.py`](tokenizer.md)  
  Loads tokenizers and provides functions to tokenize text into token IDs and attention masks.

- [`parser.py`](parser.md)  
  Parses `.pdf`, `.md`, and `.txt` files into structured `Document` objects.

- [`chunker.py`](chunker.md)  
  Splits text into manageable chunks using sentence-based or sliding window strategies.

- [`embedder.py`](embedder.md)  
  Loads sentence embedding models and encodes text chunks into vector representations.

- [`db.py`](db.md)  
  Main database handler for adding, querying, deleting, and managing documents in ChromaDB.

- [`ingest.py`](ingest.md)  
  Full ingestion pipeline: parse files → chunk text → embed → store into the vector database.

- [`query.py`](query.md)  
  User-facing interface for retrieving top relevant chunks based on a query.

- [`vectordb (client.py + controller.py)`](vectordb.md)  
  Thin wrapper over ChromaDB for client connection, collection creation, listing, and deletion.

---

## 🛠️ System Overview

The Archivum system follows this pipeline:

1. **Parsing** → Input files are parsed into documents and chunks.
2. **Chunking** → Large texts are split into smaller, manageable pieces.
3. **Embedding** → Chunks are embedded into dense vector representations.
4. **Storage** → Embeddings are stored in a ChromaDB persistent database.
5. **Querying** → Users search and retrieve relevant information using semantic similarity.

---

## 📂 Key Paths (Inside the Project)

- `archivum/`: All core system modules
- `input/`: Ingested raw files (PDFs, Markdown, Text)
- `vectordb/`: Storage for ChromaDB collections
- `assets/`: Tokenizer and other model assets
- `docs/`: Project documentation

---

