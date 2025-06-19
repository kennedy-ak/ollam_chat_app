import streamlit as st
import ollama
import PyPDF2
import docx
import io

# Set page config
st.set_page_config(page_title="Ollama Chat", page_icon="🤖", layout="wide")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session state for uploaded file content
if "file_content" not in st.session_state:
    st.session_state.file_content = ""
if "file_name" not in st.session_state:
    st.session_state.file_name = ""

# Function to extract text from PDF
def extract_pdf_text(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""

# Function to extract text from DOCX
def extract_docx_text(docx_file):
    try:
        doc = docx.Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading DOCX: {str(e)}")
        return ""

# Function to extract text from TXT
def extract_txt_text(txt_file):
    try:
        return str(txt_file.read(), "utf-8")
    except Exception as e:
        st.error(f"Error reading TXT: {str(e)}")
        return ""

# Initialize session state for selected model
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "llama3.2:latest"

# App title
st.title("🤖 Ollama Chat Assistant")

# File upload section
st.subheader("📁 Upload Document (Optional)")
uploaded_file = st.file_uploader(
    "Choose a file to analyze",
    type=['pdf', 'docx', 'txt'],
    help="Upload PDF, DOCX, or TXT files to chat about their content"
)

# Process uploaded file
if uploaded_file is not None:
    if uploaded_file.name != st.session_state.file_name:
        st.session_state.file_name = uploaded_file.name
        
        with st.spinner(f"Processing {uploaded_file.name}..."):
            if uploaded_file.type == "application/pdf":
                st.session_state.file_content = extract_pdf_text(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                st.session_state.file_content = extract_docx_text(uploaded_file)
            elif uploaded_file.type == "text/plain":
                st.session_state.file_content = extract_txt_text(uploaded_file)
            else:
                st.error("Unsupported file type")
                st.session_state.file_content = ""
        
        if st.session_state.file_content:
            st.success(f"✅ Successfully processed {uploaded_file.name}")
            st.info(f"📄 Document contains {len(st.session_state.file_content.split())} words")
            
            # Show preview of content
            with st.expander("📖 Preview document content"):
                st.text_area(
                    "Content preview:",
                    st.session_state.file_content[:1000] + ("..." if len(st.session_state.file_content) > 1000 else ""),
                    height=200,
                    disabled=True
                )
        else:
            st.error("Could not extract text from the file")

# Display current file info
if st.session_state.file_name:
    st.info(f"📎 Current file: **{st.session_state.file_name}** | You can ask questions about this document")
    if st.button("🗑️ Remove file"):
        st.session_state.file_content = ""
        st.session_state.file_name = ""
        st.rerun()

st.divider()

# Model selection
common_models = [
    "deepseek-r1:1.5b",
  # Ollama Chat Assistant

A Streamlit-based web application that allows you to chat with documents (PDF, DOCX, TXT) using local LLMs via Ollama.

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

*This project is for educational and research purposes.*# Ollama Chat Assistant

A Streamlit-based web application that allows you to chat with documents (PDF, DOCX, TXT) using local LLMs via Ollama.

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

*This project is for educational and research purposes.*
    "gemma3:4b",
]

selected_model = st.selectbox(
    "Select Model:",
    common_models,
    index=common_models.index(st.session_state.selected_model) if st.session_state.selected_model in common_models else 0,
    key="model_selector"
)

# Update session state if model changed
if selected_model != st.session_state.selected_model:
    st.session_state.selected_model = selected_model
    # Clear chat history when switching models
    if st.session_state.messages:
        st.warning(f"Switched to {selected_model}. Chat history cleared.")
        st.session_state.messages = []

st.caption(f"Currently chatting with: **{st.session_state.selected_model}**")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Prepare messages with file content if available
                messages = [{"role": "system", "content": "You are an expert assistant"}]
                
                # Add file content to system message if available
                if st.session_state.file_content:
                    file_context = f"\n\nThe user has uploaded a document '{st.session_state.file_name}' with the following content:\n\n{st.session_state.file_content}\n\nPlease use this document to answer questions when relevant."
                    messages[0]["content"] += file_context
                
                # Add conversation history
                messages.extend(st.session_state.messages)
                
                # Call Ollama with selected model
                response = ollama.chat(
                    model=st.session_state.selected_model,
                    messages=messages
                )
                
                # Extract response content
                assistant_response = response['message']['content']
                
                # Display response
                st.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.error("Make sure Ollama is running and the model is available.")

# Sidebar with options
with st.sidebar:
    st.header("Chat Options")
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    # Clear file button
    if st.session_state.file_name:
        if st.button("Clear Uploaded File"):
            st.session_state.file_content = ""
            st.session_state.file_name = ""
            st.rerun()
    
    st.divider()
    
    # File upload info
    st.subheader("📎 Supported Files")
    st.markdown("""
    - **PDF** (.pdf) - Extract text from PDF documents
    - **Word** (.docx) - Microsoft Word documents  
    - **Text** (.txt) - Plain text files
    
   
    """)
    
    st.divider()
    
    # Instructions
   
    
    # Chat statistics
    if st.session_state.messages:
        st.divider()
        st.subheader("Chat Stats")
        st.markdown(f"**Total messages:** {len(st.session_state.messages)}")
        
        # Count user vs assistant messages
        user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
        assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        
        st.markdown(f"**Your messages:** {user_msgs}")
        st.markdown(f"**AI responses:** {assistant_msgs}")
        st.markdown(f"**Current model:** {st.session_state.selected_model}")
        
        if st.session_state.file_name:
            st.markdown(f"**Document:** {st.session_state.file_name}")
            st.markdown(f"**Words in doc:** {len(st.session_state.file_content.split()) if st.session_state.file_content else 0}")