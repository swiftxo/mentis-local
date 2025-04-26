import archivum.config as config
from archivum.parser import parse_file
from archivum.tokenizer_utils import load_tokenizer
from archivum.chunker import chunk_text
from archivum.db import Archivum
import json
from pathlib import Path

# Tracker file for ingested files
INGESTED_FILES_TRACKER = Path("archivum/vectordb/ingested_files.json")

def load_ingested_files() -> set:
    """Load the set of already-ingested file paths."""
    if not INGESTED_FILES_TRACKER.exists():
        return set()
    with open(INGESTED_FILES_TRACKER, "r") as f:
        return set(json.load(f))

def save_ingested_files(files: set):
    """Save the updated set of ingested file paths."""
    with open(INGESTED_FILES_TRACKER, "w") as f:
        json.dump(list(files), f, indent=2)

def ingest(path: str = config.DATA_FOLDER):
    """Run the ingestion pipeline: parse, chunk, embed, and store ONLY new documents."""

    ingested_files = load_ingested_files()
    tokenizer = load_tokenizer()
    db = Archivum(config.VECTOR_DB_PATH, config.COLLECTION_NAME)

    new_files = []
    documents = []

    paths = Path(config.DATA_FOLDER).rglob("*")

    for file_path in paths:
        if file_path.is_file() and file_path.suffix.lower() in [".pdf", ".md", ".txt"]:
            file_path_str = file_path.as_posix()

            if file_path_str not in ingested_files:
                if config.VERBOSE:
                    print(f"[Ingest] New file detected: {file_path_str}")

                document = parse_file(file_path_str)
                documents.append((file_path_str, document))
                new_files.append(file_path_str)

    if not documents:
        print("[Ingest] No new files to ingest.")
        return

    all_chunks = []
    all_metadatas = []
    ids = []

    for doc_index, (file_path, document) in enumerate(documents):
        for chunk_index, big_chunk in enumerate(document.get_chunks()):
            small_chunks = chunk_text(big_chunk.text, tokenizer=tokenizer)

            for small_index, chunked_text in enumerate(small_chunks):
                all_chunks.append(chunked_text)
                all_metadatas.append(big_chunk.metadata)
                ids.append(f"doc{doc_index}_page{chunk_index}_chunk{small_index}")

    db.add_documents(documents=all_chunks, ids=ids, metadatas=all_metadatas)

    ingested_files.update(new_files)
    save_ingested_files(ingested_files)

    if config.VERBOSE:
        print(f"[Ingest] Ingested {len(all_chunks)} chunks from {len(new_files)} new files into collection '{config.COLLECTION_NAME}'.")
