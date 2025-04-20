
class DocumentChunk:
    def __init__(self, text: str, metadata: dict = None):
        self.text = text
        self.metadata = metadata or {}

    def __repr__(self):
        preview = self.text[:40].replace("\n", " ") + "..." if len(self.text) > 40 else self.text
        return f"DocumentChunk(text='{preview}', metadata={self.metadata})"

    def __len__(self):
        return len(self.text)

    def get_metadata(self):
        return self.metadata

    def to_dict(self):
        return {"text": self.text, "metadata": self.metadata}

class Document:
    def __init__(self, chunks: list[DocumentChunk]):
        self.chunks = chunks

    def __repr__(self):
        return f"<Document with {len(self.chunks)} chunks>"

    def __len__(self):
        return len(self.chunks)

    def get_chunks(self):
        return self.chunks

    def to_dict(self):
        return [chunk.to_dict() for chunk in self.chunks]