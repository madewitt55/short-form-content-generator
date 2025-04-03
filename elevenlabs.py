import os
from dotenv import load_dotenv

'''ElevenLabs API request information'''

load_dotenv() # Load environment variables
BASE_URL = "https://api.elevenlabs.io"
HEADERS = {
    "xi-api-key": os.getenv('ELEVEN_LABS_API_KEY')
}