# Ollama Chat Assistant

A Streamlit-based web application that allows you to chat with documents (PDF, DOCX, )
This uses local models
_

## Features

- Upload and analyze PDF, DOCX, or TXT files.
- Extracts and previews document content.
- Chat with your documents using various LLM models.
- Simple, interactive UI built with Streamlit.

## Getting Started

### Prerequisites

- Python 3.12+
- [Ollama](https://ollama.com/) installed and running locally
- Recommended: Create and activate a virtual environment

### Installation

1. Clone the repository:
    ```sh
    git clone <repo-url>
    cd ollam_chat_app
    ```

2. Activate your virtual environment:
    ```sh
    source env/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install streamlit ollama PyPDF2 python-docx
    ```

### Running the App

```sh
streamlit run main.py
```

Open the provided local URL in your browser to access the app.

## Usage

1. Upload a PDF, DOCX, or TXT file using the upload widget.
2. Preview the extracted content.
3. Select a model from the dropdown.
4. Start chatting and ask questions about your document.

## Project Structure

- `main.py` — Main Streamlit application.
- `env/` — Python virtual environment (not included in version control).

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Ollama Python SDK](https://github.com/jmorganca/ollama)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [python-docx](https://python-docx.readthedocs.io/)

## License

MIT License

---

*This project is for educational and research purposes, you are allowed to build upon it*