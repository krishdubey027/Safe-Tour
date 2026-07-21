import os
from dotenv import load_dotenv

# Load variables from a .env file if it exists
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'safetour_secret_session_key_12345')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/safetour')
    
    # API credentials (optional, can fallback to simulation)
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', '')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY', '')
