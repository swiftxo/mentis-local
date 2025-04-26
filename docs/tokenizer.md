# Module: `tokenizer_utils.py`

## Purpose
Handles loading a tokenizer from file and provides utility functions to tokenize text into token IDs and attention masks, or retrieve raw encodings.

---

## Functions

#### `load_tokenizer`
- **Description**: Loads a tokenizer from a saved file and enables padding and truncation according to config settings.
- **Parameters**:  
  - `path` (str, optional): Path to the tokenizer file. Defaults to `config.TOKENIZER_PATH`.
- **Returns**:  
  - `Tokenizer`: An initialized `Tokenizer` object ready for tokenization.
- **Notes**:  
  - Verbose logging is available if `config.VERBOSE` is enabled.

---

#### `tokenize`
- **Description**: Tokenizes input text into token IDs and attention masks.
- **Parameters**:  
  - `text` (str): The input text to tokenize.  
  - `tokenizer` (`Tokenizer`): A pre-loaded tokenizer object.
- **Returns**:  
  - `Tuple[List[int], List[int]]`: A tuple containing the token IDs and the attention mask.
- **Notes**:  
  - Debug logging is available if `config.DEBUG` is enabled.

---

#### `tokenize_raw`
- **Description**: Tokenizes input text and returns the raw `Encoding` object.
- **Parameters**:  
  - `text` (str): The input text to tokenize.  
  - `tokenizer` (`Tokenizer`): A pre-loaded tokenizer object.
- **Returns**:  
  - `Encoding`: The raw encoding result, including token IDs, masks, etc.
- **Notes**:  
  - Useful if you need access to more detailed tokenization data beyond IDs and masks.

---

## Dependencies
- `os`
- `tokenizers` (from HuggingFace's `tokenizers` library)
- `typing` (`Tuple`, `List`)
- `archivum.config` (local module for configuration settings)

---

## Config Settings
- `config.VERBOSE`: Enables verbose logging.
- `config.DEBUG`: Enables detailed debug logs.
- `config.TOKENIZER_PATH`: Default path to load the tokenizer file.
- `config.TOKENIZER_MAX_LENGTH`: Maximum token length for padding/truncation.
- `config.TOKENIZER_PAD_ID`: ID used for padding tokens.
- `config.TOKENIZER_PAD_TOKEN`: String token used for padding.

