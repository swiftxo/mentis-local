import pymupdf
import json
from .document import Document, DocumentChunk
from pathlib import Path
import archivum.config as config

VERBOSE = config.VERBOSE
DEBUG = config.DEBUG

def parse_pdf(file_path):
    """Parses a PDF file and returns a Document object containing the DocumentChunks which contain the text and metadata."""
    if VERBOSE:
        print(f"[Parser|PDF] Parsing file: {file_path}")

    pdf = pymupdf.open(file_path)
    pdf_chunks = []
    for page_num, page in enumerate(pdf, start=1):
        text = page.get_text("text").strip()
        if text:
            metadata = {
                "page_number": page_num,
                "file_path": file_path,
                "file_type": "pdf"
            }
            chunk = DocumentChunk(text, metadata)
            pdf_chunks.append(chunk)
    pdf.close()

    if VERBOSE:
        print(f"[Parser|PDF] Parsed {len(pdf_chunks)} pages with text.")

    return Document(pdf_chunks)

def parse_md(file_path):
    """Parses a Markdown file and returns a Document object containing the DocumentChunks which contain the text and metadata."""
    if VERBOSE:
        print(f"[Parser|MD] Parsing file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        metadata = {
            "file_path": file_path,
            "file_type": "md"
        }
        chunk = DocumentChunk(text, metadata)
    
    if VERBOSE:
        print(f"[Parser|MD] Parsed markdown file into one chunk.")

    return Document([chunk])

def parse_txt(file_path):
    """Parses a text file and returns a Document object containing the DocumentChunks which contain the text and metadata."""
    if VERBOSE:
        print(f"[Parser|TXT] Parsing file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        metadata = {
            "file_path": file_path,
            "file_type": "txt"
        }
        chunk = DocumentChunk(text, metadata)
    
    if VERBOSE:
        print(f"[Parser|TXT] Parsed text file into one chunk.")

    return Document([chunk])

def parse_file(file_path):
    """Parses a file based on its extension and returns a Document object containing the DocumentChunks which contain the text and metadata."""
    ext = Path(file_path).suffix.lower()

    if VERBOSE:
        print(f"[Parser|Dispatch] File extension detected: {ext}")

    if ext == ".pdf":
        return parse_pdf(file_path)
    elif ext == ".md":
        return parse_md(file_path)
    elif ext == ".txt":
        return parse_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def parse_folder(folder_path):
    """Parses all files in a folder and returns a list of Document objects containing the DocumentChunks which contain the text and metadata."""
    
    supported_extensions = [".pdf", ".md", ".txt"]
    documents = []
    paths = Path(folder_path).rglob("*")

    if VERBOSE:
        print(f"[Parser|Folder] Parsing folder: {folder_path}")

    for file_path in paths:
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            if VERBOSE:
                print(f"[Parser|Folder] Supported file found: {file_path}")

            document = parse_file(file_path.as_posix())
            documents.append(document)

    if VERBOSE:
        print(f"[Parser|Folder] Total documents parsed: {len(documents)}")

    if DEBUG:
        print(f"[Parser|Folder|DEBUG] Document details: {[str(doc) for doc in documents]}")

    return documents
