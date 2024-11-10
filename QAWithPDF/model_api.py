import os
from dotenv import load_dotenv
import sys
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import CustomException
from logger import logging
from llama_index.llms.gemini import Gemini

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Debugging: Check if the API key loaded successfully
if GEMINI_API_KEY:
    logging.info("API Key successfully loaded.")
else:
    logging.error("API Key not loaded. Check the .env file for correctness.")

# Configure the Google Generative AI API with the loaded API key
try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    logging.error(f"Failed to configure genai with the API key: {e}")
    raise CustomException(e, sys)

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        # Initialize the Gemini model
        model = Gemini(models='gemini-pro', api_key=GEMINI_API_KEY)
        logging.info("Gemini model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error loading Gemini model: {e}")
        raise CustomException(e, sys)

