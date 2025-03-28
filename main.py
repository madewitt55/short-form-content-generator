import os
from dotenv import load_dotenv
load_dotenv()
import requests

BASE_URL = "https://api.elevenlabs.io"
headers = {
    "xi-api-key": os.getenv('ELEVEN_LABS_API_KEY')
}

# Takes an error response and generates a readable exception
def GenerateException(response):
    return Exception(f'Failed with status {response.status_code}: '
        f'{response.json()['detail']['message']}')

# Returns all cloned voices in an array of dicts with id and name
def GetClonedVoices():
    response = requests.get(BASE_URL + "/v2/voices?category=cloned", 
        headers=headers)
    if (response.status_code != 200):
        raise GenerateException(response)
    
    # Populate and return array
    voices = []
    for v in response.json()['voices']:
        voices.append({'id': v['voice_id'], 'name': v['name']})
    return voices

def Main():
    if (not os.getenv('ELEVEN_LABS_API_KEY')):
        return print('API key not found')
    try:
        print(GetClonedVoices())
    except Exception as e:
        return print(e)

Main()