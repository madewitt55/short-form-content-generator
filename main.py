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
    Args:
        None

    Returns:
        Array of ElevenLabs response voice models
    '''

    response = requests.get(el.BASE_URL + "/v2/voices", 
        headers=el.HEADERS)
    response.raise_for_status() # Throws error if status 4xx or 5xx
    return response.json()['voices']

def Main():
    if (not os.getenv('ELEVEN_LABS_API_KEY')):
        raise ValueError('API key not found')
    try:
        voices = GetVoices()
        if (len(voices) < 2):
            raise ValueError(f'{len(voices)} voices found. At least 2 voices'
                'are required to use this script.')
        
        print('========== Cloned Voices ==========')
        for i in range(len(voices)):
            if (voices[i]['category'] == 'cloned'):
                print(f'{i}: {voices[i]['name']}')
            else:
                break

        if (i >= 1):
            choice = input('\nShow non-cloned voices? (Y/N)')
        if (choice.upper() == 'Y' or i < 1):
            print('\n========== Standard Voices ==========')
            for j in range(i, len(voices)):
                print(f'{j}: {voices[j]['name']}')

        choice = 0
        voice1 = None
        voice2 = None
        while (not voice1 or not voice2):
            choice = int(input('Select voice: '))
            if (choice < 0 or choice >= len(voices)):
                print('INVALID INPUT')
            elif (voice1 == None):
                voice1 = Voice(voices[choice])
                print(f'Voice 1 ID: {voice1.voice_id}')
            else:
                voice2 = Voice(voices[choice])
                print(f'Voice 2 ID: {voice2.voice_id}')

        print(voice1.name)
        print(voice2.name)
                


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