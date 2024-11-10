from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.core import StorageContext , load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from QAWithPDF.data_ingestion  import load_data
from QAWithPDF.model_api  import load_model
import sys
from  exception import CustomException
from logger import logging



def download_gemini_embedding(model,documents):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        embeddings = GeminiEmbedding(model_name="models/embedding-001")
        Settings.llm = model
        Settings.embed_model = embeddings
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
        logging.info("")
        index = VectorStoreIndex.from_documents(documents, embed_model=embeddings, llm=model)
        index.storage_context.persist()
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise CustomException(e,sys)
    


