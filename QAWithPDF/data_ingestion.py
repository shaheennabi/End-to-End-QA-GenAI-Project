from llama_index.core import SimpleDirectoryReader
import sys
from exception import CustomException
from logger import logging

def load_data(data):
    """
    Loading the documents from a specified  directory

    Parameters: 
    - data (str): The path to the directory containing files

    Returns: 
    - A list of loaded documents. The specific type of documents may vary.
    
    """
    try: 
        logging.info("data loading started...")
        loader=SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception is loading data...")
        return CustomException(e,sys)
    

    