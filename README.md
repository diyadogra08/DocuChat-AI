📄 DocuChat AI

DocuChat AI is a PDF question-answering application built using Python, Streamlit, and Ollama. It allows users to upload a PDF document and ask questions about its content using a local AI model.

✨ Features

- 📂 Upload PDF documents
- 📖 Extract and preview PDF text
- 💬 Ask questions about the uploaded document
- 🤖 Generate answers using the Ollama language model
- 🔒 Process documents locally on your computer

🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Requests
- Ollama
- Llama 3.2 (1B)

⚙️ Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

Replace "YOUR_GITHUB_REPOSITORY_URL" with your repository's actual URL.

2. Open the project folder

cd DocuChat-AI

3. Install dependencies

python -m pip install -r requirements.txt

4. Install and start Ollama

Install Ollama from https://ollama.com if it is not already installed.

Download the model:

ollama pull llama3.2:1b

5. Run the application

python -m streamlit run app.py

Open the local URL displayed in the terminal, usually "http://localhost:8501".

🚀 Future Improvements

- Improve answers for long PDF documents
- Add chat history
- Support multiple document formats
- Improve document search and retrieval

👩‍💻 Author

Created as a beginner-friendly AI project to explore Python, document processing, and local language models.

📌 Note

This project currently runs locally and requires Ollama and the specified model to be installed. Uploading the repository to GitHub does not automatically deploy the application online.
