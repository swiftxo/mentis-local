from archivum.db import Archivum
import archivum.config as config
from archivum.ingest import ingest
from archivum.query import retrieve_relevant_chunks, retrieve_chunks_with_metadata
import json
# Connect to your existing ChromaDB storage and collection
db = Archivum(
    storage_path=config.VECTOR_DB_PATH,
    collection_name=config.COLLECTION_NAME
)

ingest()




query_text = input("Enter your query: ")
chunks = retrieve_chunks_with_metadata(query_text, n_results=5)

# Step 4: Print retrieved chunks
print("\n=== Retrieved Chunks ===")
for idx, chunk in enumerate(chunks, 1):
    print(f"Chunk {idx}:")
    print(f"Text: {chunk['text']}")
    print(f"Metadata: {json.dumps(chunk['metadata'], indent=2)}")
    print(f"Distance: {chunk['distance']}")
    print("-" * 40)