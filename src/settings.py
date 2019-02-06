from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Gets secure API and DB information from the .env file and stores it in our assigned variable. 
SECRET_KEY = os.getenv("API_KEY")
BITLY_API_USER = os.getenv("BITLY_API_USER")
BITLY_API_KEY = os.getenv("BITLY_API_KEY")
YTDATA_API_KEY = os.getenv("YTDATA_API_KEY")
FTLIVE_AUTH_TOKEN = os.getenv("FTLIVE_AUTH_TOKEN")
GCS_API_KEY = os.getenv("GCS_API_KEY")
GCS_ENGINE_ID = os.getenv("GCS_ENGINE_ID")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")