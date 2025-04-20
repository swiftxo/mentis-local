# 🧭 Design principles


### 1. **Full Stack Transparency**

> Every component of the system — from file ingestion to chunking, embedding, and querying — should be understandable and, if needed, modifiable. Nothing should be a black box.


### 2. **Low-Level Parsing Control**

> The system should not depend exclusively on high-level or proprietary parsers. File parsing should be configurable and extensible, with an emphasis on understanding how data is extracted from raw formats.



### 3. **Modular & Replaceable Design**

> Each core function (e.g., ingestion, chunking, embedding, vector storage, querying) should be separated and replaceable. This ensures long-term maintainability and allows experimenting with alternative approaches without rewriting everything.



### 4. **Minimal Dependency Philosophy**

> Default to open-source, local, and minimal libraries. Only introduce higher-level tools like `llama-index` or LangChain if they add genuine value or speed up early development — but they should be easy to remove or swap later.



### 5. **Educational by Design**

> This project is a tool _for learning_, not just building. Every design choice should prioritize clarity and offer insights into systems design, information retrieval, and language model behavior.



### 6. **Beyond a GPT Wrapper**

> Mentis is not just another GPT interface. Its purpose is to become a meaningful interface to **structured personal knowledge** — powered by embeddings and retrieval, not just chat completions.



### 7. **Built for Local Autonomy**

> Mentis should function fully offline and locally, respecting user privacy and data control. LLMs, vector stores, and documents should be usable without internet or cloud APIs.