import requests
from speech import Speech
import elevenlabs as el
import json

# Import character settings from settings.json
with open("character_settings.json", "r") as file:
    character_settings = json.load(file)

class Voice:
    '''A character's voice'''

    def __init__(self, voice):
        '''
        Constructs a new voice

        Args: 
            voice (dict): ElevenLabs API response voice model

        Returns:
            void
        '''
        
        self.voice_id = voice['voice_id']

        if (character_settings.get(self.voice_id, {}).get('name')):
            # Load user-defined custom name
            self.name = character_settings[self.voice_id]['name']
        else:
            self.name = voice['name']

        self.image_path = character_settings.get(self.voice_id, {}).get('image_path')
        self.image_position = character_settings.get(self.voice_id, {}).get('image_position')

    def CreateSpeech(self, text):
        '''
        Creates a synthesized speech instance through ElevenLabs

        Args:
            voice_id (string): ID of the voice in which speech should be created
            text (string): Text of the speech to be created

        Returns:
            Speech: New speech instance
        '''
        if (len(text) < 3 or len(text) > 150):
            raise ValueError('Length of voice line must be between 3 and 100'
            ' characters')
        
        response = requests.post(el.BASE_URL + f"/v1/text-to-speech/{self.voice_id}/with-timestamps",
            headers=el.HEADERS,
            json={
                "text": f"{text}"
            })
        response.raise_for_status() # Throws error if status 4xx or 5xx
        return Speech(self, response.json())
    