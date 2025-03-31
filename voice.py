import requests
from speech import Speech
import elevenlabs as el


class Voice:
    '''A character's voice'''

    def __init__(self, voice):
        '''
        Constructs a new voice
        Args: 
            voice (dict): ElevenLabs API response voice model
        Returns:
            void

        Initalizes voice_id and name, as well as voice_lines, traits, and
        nicknames if they are found
        '''
        
        self.voice_id = voice['voice_id']
        self.name = voice['name']

        '''self.voice_lines = cq.voice_lines.get(self.name)
        self.traits = cq.traits.get(self.name)
        self.nicknames = cq.nicknames.get(self.name)'''

    def CreateSpeech(self, text):
        '''
        Creates a synthesized speech instance through ElevenLabs
        Args:
            voice_id (string): ID of the voice in which speech should be created
            text (string): Text of the speech to be created
        Returns:
            Speech: New speech instance
        '''
        if (len(text) < 3 or len(text) > 100):
            raise ValueError('Length of voice line must be between 3 and 100'
            'characters')
        
        response = requests.post(el.BASE_URL + f"/v1/text-to-speech/{self.voice_id}/with-timestamps",
            headers=el.HEADERS,
            json={
                "text": f"{text}"
            })
        response.raise_for_status() # Throws error if status 4xx or 5xx
        return Speech(self, response.json())
    