import streamlit as st
import requests
from pypdf import PdfReader

st.set_page_config(
    page_title="DocuChat AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 DocuChat AI")
st.caption("Upload a PDF and chat with its content using AI.")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"

uploaded_file = st.file_uploader(
    "📂 Upload your PDF",
    type=["pdf"]
)

if uploaded_file:
    try:
        reader = PdfReader(uploaded_file)
        pdf_text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

        if not pdf_text.strip():
            st.warning(
                "No readable text found. Try a text-based PDF."
            )
        else:
            st.success(
                f"PDF ready! Total pages: {len(reader.pages)}"
            )

            with st.expander("Preview PDF text"):
                st.text_area(
                    "Extracted content",
                    pdf_text[:10000],
                    height=200
                )

            question = st.text_input(
                "💬 Ask a question about your PDF"
            )

            if st.button("Generate Answer"):
                if not question.strip():
                    st.warning("Please enter a question.")
                else:
                    # Keep the prompt within a manageable size.
                    context = pdf_text[:12000]

                    prompt = f"""
You are a helpful document assistant.
Answer the question using only the PDF content below.
If the answer is not present, say that you could not find it
in the provided document. Do not invent facts.

PDF CONTENT:
{context}

QUESTION:
{question}

ANSWER:
"""

                    try:
                        with st.spinner("AI is reading your document..."):
                            response = requests.post(
                                OLLAMA_URL,
                                json={
                                    "model": MODEL,
                                    "prompt": prompt,
                                    "stream": False
                                },
                                timeout=180
                            )
                            response.raise_for_status()
                            answer = response.json().get(
                                "response", ""
                            )

                        st.subheader("🤖 AI Answer")
                        st.write(answer or "No answer generated.")

                    except requests.exceptions.ConnectionError:
                        st.error(
                            "Ollama is not running. Open a terminal "
                            "and run: ollama serve"
                        )
                    except requests.exceptions.Timeout:
                        st.error(
                            "The AI took too long to respond. "
                            "Please try again."
                        )
                    except requests.exceptions.RequestException as error:
                        st.error(f"AI request failed: {error}")

    except Exception as error:
        st.error(f"Could not read the PDF: {error}")