
# ========== Vectorstore / Database Settings ==========
VECTOR_DB_PATH = "/Users/soho/Archivum/code/mentis-local/archivum/vectordbb"            # Where ChromaDB will store collections
COLLECTION_NAME = "archivum_fragments"    # Default collection name to create/use
DATA_FOLDER = '/Users/soho/Archivum/code/mentis-local/input/sample'


# ========== Embedding Settings ==========
EMBED_MODEL_NAME = "intfloat/multilingual-e5-large-instruct"  # Model to load
EMBED_BATCH_SIZE = 32          # (OPTIONAL) Batch size if you want to add batching later
EMBED_NORMALIZE = True         # Normalize embeddings to unit length
EMBED_AS_TENSOR = False         # Return as PyTorch tensor (True) or numpy array (False)
EMBED_DEVICE = "auto"          # "auto" = detect GPU, else CPU. Can force "cuda" or "cpu".
EMBED_TIMEOUT = 60             # Max seconds to wait per batch (rarely needed)

# ========== Chunking Settings ==========
CHUNK_METHOD = "sentence" # Options: "sentence", "sliding_window"
CHUNK_MAX_TOKENS = 512
CHUNK_WINDOW = 150                   # Window size for sliding window chunking
CHUNK_STRIDE = 30                    # Step size for sliding window
CHUNK_MIN_TOKENS = 10                # Minimum tokens to keep a chunk (skip smaller)
CHUNK_LOGGING = False                # Whether to print debug info during chunking


# ========== Tokenizer Settings ==========
TOKENIZER_PATH = "assets/tokenizer.json"  # Path to the tokenizer JSON file
TOKENIZER_PAD_ID = 1                      # Token ID to use for padding
TOKENIZER_PAD_TOKEN = "<pad>"              # Token string for padding
TOKENIZER_MAX_LENGTH = 512                 # Max tokens per input (for padding/truncation)


### ========== General Settings ==========
VERBOSE = True  # Print debug info
DEBUG = False  # Print debug info
