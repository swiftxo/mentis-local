import pymupdf, json
from .document import Document, DocumentChunk
from pathlib import Path

def parse_pdf(file_path):
    """
    Parses a PDF file and returns a Document object containing the DocumentChunks which contain the text and metadata.

    Args:
        file_path (str): The path to the PDF file.
    Returns:
        Document: A Document object containing the parsed text and metadata.
    """

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
    document = Document(pdf_chunks)
    return document


def parse_md(file_path):
    """
    Parses a Markdown file and returns a Document object containing the DocumentChunks which contain the text and metadata.

    Args:
        file_path (str): The path to the Markdown file.
    Returns:
        Document: A Document object containing the parsed text and metadata.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        metadata = {
            "file_path": file_path,
            "file_type": "md"
        }
        chunk = DocumentChunk(text, metadata)
        document = Document([chunk])
    return document


def parse_txt(file_path):
    """
    Parses a text file and returns a Document object containing the DocumentChunks which contain the text and metadata.

    Args:
        file_path (str): The path to the text file.
    Returns:
        Document: A Document object containing the parsed text and metadata.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        metadata = {
            "file_path": file_path,
            "file_type": "txt"
        }
        chunk = DocumentChunk(text, metadata)
        document = Document([chunk])
    return document


def parse_file(file_path):
    """
    Parses a file based on its extension and returns a Document object containing the DocumentChunks which contain the text and metadata.

    Args:
        file_path (str): The path to the file.
    Returns:
        Document: A Document object containing the parsed text and metadata.
    """

    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return parse_pdf(file_path)
    elif ext == ".md":
        return parse_md(file_path)
    elif ext == ".txt":
        return parse_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")