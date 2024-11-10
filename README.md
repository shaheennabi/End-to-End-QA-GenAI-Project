# End-to-End QA GenAI Project

This project implements a **Retrieval-Augmented Generation (RAG)** system with a **Streamlit UI** for uploading PDF documents. It integrates the **Google Gemini API** (using the Gemini Pro model) for high-performance natural language understanding and generation. The **LlamaIndex** framework is used for efficient document indexing and retrieval.

## Features

- **Streamlit UI** for seamless PDF uploads and interactions.
- **Google Gemini API** integration for powerful language generation using the Gemini Pro model.
- **LlamaIndex** framework for fast and scalable document indexing and retrieval.
- Modular code structure for maintainability and ease of use.

## Architecture

The project is designed to be modular, enabling scalability and ease of maintenance. Below are the key components:

1. **Streamlit UI**: Allows the user to upload PDF files and interact with the system.
2. **Document Preprocessing**: Extracts text from PDFs and prepares them for indexing.
3. **LlamaIndex Integration**: Indexes documents for fast retrieval.
4. **Google Gemini API**: Uses the Gemini Pro model for query generation and response.
5. **Modular Code Structure**: Each component is separated into different modules for reusability and ease of modification.

## Setup

To get started with this RAG system, follow the steps below:

### Prerequisites

- Python 3.9 or higher.
- Google Gemini API credentials.
- LlamaIndex library.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shaheennabi/End-to-End-QA-GenAI-Project.git
   cd End-to-End-QA-GenAI-Project
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python3.9 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your **Google Gemini API** credentials. Follow [Google's official documentation](https://cloud.google.com/docs/authentication/getting-started) for setting up the API credentials.

5. Install **LlamaIndex**:

   ```bash
   pip install llama-index
   ```

### Running the Application

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and visit `http://localhost:8501` to interact with the app.

3. Upload a PDF file and interact with the system to generate answers to your queries.

## Workflow

1. **Upload PDF**: Users upload a PDF via the Streamlit UI.
2. **Text Extraction**: The PDF content is extracted into text.
3. **Document Indexing**: The extracted text is indexed using LlamaIndex.
4. **Query Generation**: Users submit a query, which is processed by the **Google Gemini Pro** model.
5. **Results**: Relevant information from the documents is retrieved, and the response is generated using the Gemini API.

## API Integration

This project utilizes the **Google Gemini API** (Gemini Pro model) to process and generate responses based on the query. To use the API, you must set up your **Google Gemini API** credentials as outlined in the `config.py` file.

## Future Enhancements

- **Multilingual Support**: Extend the system to support multiple languages for text generation.
- **Document Summarization**: Implement automatic summarization for lengthy documents.
- **Advanced Search Features**: Add more advanced search functionality for document retrieval.

## Contributing

We welcome contributions to improve this project. To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Open a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
