import requests
import os
from voice import Voice
import elevenlabs as el
from dialogue import Dialogue

def GetClonedVoices():
    '''
    Fetches and returns a user's cloned voices
    Args: N/A
    Returns:
        [Voice]: Array of Voice objects
    '''

    response = requests.get(el.BASE_URL + "/v2/voices?category=cloned", 
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
        voices = GetClonedVoices()
        if (len(voices)):
            voice1 = voices[0]
            voice2 = voices[1]
            d = Dialogue(voice1, voice2, "Yo whats up mr white wanna cook bitch?/Jesse go fucking kill yourself retard")
            d.CreateAllSpeech()

    except requests.exceptions.HTTPError as e:
        # Failed with status [status]: [message]
        return print(f'Failed with status {e.response.status_code}:'
        f' {e.response.json()['detail']['message']}')
    except NameError as e:
        print(e)
    except OSError:
        print('A system error has occured')

Main()