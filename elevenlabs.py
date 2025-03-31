import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.elevenlabs.io"
HEADERS = {
    "xi-api-key": os.getenv('ELEVEN_LABS_API_KEY')
}