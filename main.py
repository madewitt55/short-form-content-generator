import os
import base64
from dotenv import load_dotenv
load_dotenv()
import requests
from voice import Voice

BASE_URL = "https://api.elevenlabs.io"
headers = {
    "xi-api-key": os.getenv('ELEVEN_LABS_API_KEY')
}

# Takes an error response and generates a readable exception
def GenerateException(response):
    return Exception(f'Failed with status {response.status_code}: '
        f'{response.json()['detail']['message']}')

# Returns all cloned voices
def GetClonedVoices():
    response = requests.get(BASE_URL + "/v2/voices?category=cloned", 
        headers=headers)
    response.raise_for_status() # Throws error if status 4xx or 5xx
    voices = []
    for v in response.json()['voices']:
        voices.append(Voice(v))
    return voices

def CreateSpeech(voice_id, text):
    response = requests.post(BASE_URL + f"/v1/text-to-speech/{voice_id}/with-timestamps",
        headers=headers,
        json={
            "text": f"{text}"
        })
    if (response.status_code != 200):
        raise GenerateException(response)
    return response


def ConvertToMp3(base_64_string, output_path='./audio/output.mp3'):
    mp3_data = base64.b64decode(base_64_string)
    with open(output_path, "wb") as mp3_file:
        mp3_file.write(mp3_data)

def Main():
    if (not os.getenv('ELEVEN_LABS_API_KEY')):
        return print('API key not found')
    try:
        voices = GetClonedVoices()
        if (len(voices)):
            print(voices[0].name)
            #response = CreateSpeech(voices[1]['voice_id'], 'Hello my fellow YN')
            #ConvertToMp3(response.json()['audio_base64'])

    except requests.exceptions.HTTPError as e:
        return print(f'Failed with status {e.response.status_code}: '
        f'{e.response.json()['detail']['message']}')

Main()