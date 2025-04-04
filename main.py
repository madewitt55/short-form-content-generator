import requests
import os
from voice import Voice
import elevenlabs as el
from dialogue import Dialogue
from video import Video
import json

# Import character settings from character_settings.json
with open("character_settings.json", "r") as file:
    character_settings = json.load(file)

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

def Menu(voices):
    '''
    Prints a menu listing voices, allowing the user to choose two
    
    Args:
        voices [ElevenLabs response voice model]
    
    Returns:
        [Voice]: Array of Voice objects
    '''
    # Display cloned voices
    print('========== Cloned Voices ==========')
    for i in range(len(voices)):
        if (voices[i]['category'] == 'cloned'):
            print(f'{i}: {voices[i]['name']}', end='')
            if (character_settings.get(voices[i]['voice_id'], {}).get('name')):
                print(f' ({character_settings[voices[i]['voice_id']]['name']})')
            else:
                print('')
        else:
            break

    # Display non-cloned voices if user choose or if user has less than 2 
    # cloned voices
    if (i >= 1):
        choice = input('\nShow non-cloned voices? (Y/N)')
    if (choice.upper() == 'Y' or i < 1):
        print('\n========== Standard Voices ==========')
        for j in range(i, len(voices)):
            print(f'{j}: {voices[j]['name']}')
            if (character_settings.get(voices[j]['voice_id'], {}).get('name')):
                print(f' ({character_settings[voices[j]['voice_id']]['name']})')
            else:
                print('')

    choice = 0
    selected_voices = []
    while (len(selected_voices) < 2):
        choice = int(input('Select voice: '))
        if (choice < 0 or choice >= len(voices)):
            print('INVALID INPUT')
        else:
            selected_voices.append(Voice(voices[choice]))
            print(f'Voice ID: {selected_voices[-1].voice_id}')
    return selected_voices

def Main():
    '''
    Main process of the application. Allows users to ...

    Args:
        None
    
    Returns:
        void
    '''
    if (not os.getenv('ELEVEN_LABS_API_KEY')):
        raise ValueError('API key not found')
    try:
        voices = GetVoices() # Fetch voices from ElevenLabs
        if (len(voices) < 2):
            raise ValueError(f'{len(voices)} voices found. At least 2 voices'
                'are required to use this script.')
        
        selected_voices = Menu(voices) # User selects two voices from menu
        #d = Dialogue(selected_voices, 'Testing testing 123 hello hello hello hi/hello')
        #v = Video('helloworld', d)

        #print(v.GetCaptions(v.dialogue.speech_lines[0], 3))

        #selected_voices = [Voice(voices[53]), Voice(voices[56])]

        video_title = ''
        while (os.path.exists(os.path.join(os.getcwd(), f'videos/{video_title}')) or
               len(video_title) < 3 or len(video_title) > 25):
            video_title = input('Enter video title: ')
    
        script = input('Input a script'
            '(character breaks are indicated by forward slashes):\n')
        d = Dialogue(selected_voices, script)
        v = Video(video_title, d)

    # API response with status code 4xx or 5xx
    except requests.exceptions.HTTPError as e:
        # Failed with status {status}: {message}
        return print(f'Failed with status {e.response.status_code}:'
        f' {e.response.json()['detail']['message']}')
    except NameError as e:
        print(e)
    except OSError as e:
        print(e)
        print('A system error has occured')
    except ValueError as e:
        print(e)

Main() # Begin execution
