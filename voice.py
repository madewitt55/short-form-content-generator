import character_qualities as cq

class Voice:
    '''A character's voice'''

    def __init__(self, voice):
        '''
        Constructs a new voice
        Args: 
            voice: ElevenLabs API response voice object

        Initalizes voice_id and name, as well as voice_lines, traits, and
        nicknames if they are found
        '''

        if ('voice_id' not in voice or 'name' not in voice):
            raise ValueError('Unable to construct voice object due to missing'
                'voice_id or name')
        
        self.voice_id = voice['voice_id']
        self.name = voice['name']

        self.voice_lines = cq.voice_lines.get(self.name)
        self.traits = cq.traits.get(self.name)
        self.nicknames = cq.nicknames.get(self.name)

    