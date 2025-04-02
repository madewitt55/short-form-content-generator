import requests
import os
from voice import Voice
import elevenlabs as el
from dialogue import Dialogue
from video import Video
from moviepy.editor import VideoFileClip, AudioFileClip

def GetVoices():
    '''
    Fetches and returns a user's available voices
    Args: N/A
    Returns:
        [Voice]: Array of Voice objects
    '''

    response = requests.get(el.BASE_URL + "/v2/voices", 
        headers=el.HEADERS)
    response.raise_for_status() # Throws error if status 4xx or 5xx
    voices = []
    for v in response.json()['voices']:
        voices.append(Voice(v))
    return voices

def Main():
    if (not os.getenv('ELEVEN_LABS_API_KEY')):
        return print('API key not found')
    try:
        voices = GetVoices()
        if (len(voices)):
            voice1 = voices[43]
            voice2 = voices[42]
            d = Dialogue(voice1, voice2, "hello mr white how are you today?/I am doing amazing jesse!")
            v = Video('new', d)

    except requests.exceptions.HTTPError as e:
        # Failed with status [status]: [message]
        return print(f'Failed with status {e.response.status_code}:'
        f' {e.response.json()['detail']['message']}')
    except NameError as e:
        print(e)
    except OSError as e:
        print(e)
        print('A system error has occured')
    except ValueError as e:
        print(e)

Main()