Document QA Assistant
An interactive Streamlit application that lets you:

Upload PDFs, Word docs, or text files

Paste plain text directly

Crawl content from a website URL

Chunk and embed the content with sentence-transformers

Build a FAISS index for similarity search

Ask natural language questions about the uploaded or crawled content using Gemini (Google Generative AI)

Features
Document/text/website ingestion

Automatic text chunking & embedding

Fast similarity search using FAISS

Gemini-powered answers using top-matching context

Setup Instructions
1. Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
2. Install Dependencies
pip install -r requirements.txt
pip install streamlit sentence-transformers faiss-cpu google-generativeai beautifulsoup4 requests python-dotenv
3. Configure Google Gemini API
Create a .env file in the root directory:
GOOGLE_API_KEY=your_gemini_api_key_here
Get your key from https://ai.google.dev
4. Run the App
streamlit run app.py
Project Structure
.
├── app.py                  # Main Streamlit UI
├── docs_to_chunks.py       # File/plain text embedding
├── webscraper.py           # URL crawling and embedding
├── faiss_index.py          # FAISS index creation/loading
├── gemini_flash.py         # Gemini LLM interaction
├── vector_db/              # Stores embeddings and chunks
│   ├── embeddings.npy
│   └── chunks.pkl
├── .env                    # Your API key
└── README.md
Example Use Case
Upload report.pdf, paste a webpage, or drop raw text.

Click Process to chunk + embed.

Click Create Index to build the FAISS search structure.

Ask a question like:

"What are the key takeaways from the report?"

See the Gemini-generated answer using relevant context.

Tech Stack
streamlit – Web UI

sentence-transformers – Text embeddings

faiss – Vector similarity search

google-generativeai – Gemini API for natural language responses

beautifulsoup4 – HTML parsing for URLs

Notes
Index and chunks are overwritten each time — modify for persistent multi-file support if needed.

Crawling is limited to 10 pages per domain (can be changed in webscraper.py).

Ensure your documents are UTF-8 encoded if using .txt.