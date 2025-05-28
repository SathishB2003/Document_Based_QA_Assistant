import streamlit as st
import sys

# Workaround for PyTorch inspection error on Streamlit startup
sys.modules["torch.classes"] = None

from docs_to_chunks import process_uploaded_files, process_plain_text
from web_scraper import process_url_content
from faiss_index import create_index, load_index_and_chunks
from gemini_flash import get_llm_response

st.set_page_config(page_title="📄 Smart Information Retrieval and Response Generation with RAG", layout="wide")
st.title("📚 Smart Information Retrieval and Response Generation with RAG")

# --- Upload Section ---
st.header("1️⃣ Upload Files / Enter Text / URL")

uploaded_files = st.file_uploader(
    "Upload PDF, DOCX, TXT or Excel Files ", 
    type=["pdf", "docx", "txt","xlsx","xls"], 
    accept_multiple_files=True
)

plain_text = st.text_area("Or paste plain text")

url_input = st.text_input("Or enter a website URL to crawl and embed")

if st.button("🔄 Process"):
    with st.spinner("Processing input..."):
        try:
            if uploaded_files:
                msg = st.session_state["msg"] = process_uploaded_files(uploaded_files)
            elif plain_text.strip():
                msg = st.session_state["msg"] = process_plain_text(plain_text)
            elif url_input.strip():
                msg = st.session_state["msg"] = process_url_content(url_input.strip())
            else:
                msg = "⚠️ Please upload a file, enter plain text, or paste a URL."
            st.success(msg)
        except Exception as e:
            st.error(f"Error during processing: {e}")

# --- Indexing Section ---
st.header("2️⃣ Build FAISS Index")

if st.button("📌 Create Index"):
    with st.spinner("Building FAISS index..."):
        try:
            msg = create_index()
            st.success(msg)
        except Exception as e:
            st.error(f"Indexing failed: {e}")

# --- Q&A Section ---
st.header("3️⃣ Ask a Question")

question = st.text_input("Ask something based on your documents or URL:")

if st.button("🔍 Get Answer"):
    if not question.strip():
        st.warning("❗ Please enter a question.")
    else:
        try:
            index, chunks = load_index_and_chunks()
            with st.spinner("Querying Gemini..."):
                answer = get_llm_response(index, chunks, question)
            st.success("Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
