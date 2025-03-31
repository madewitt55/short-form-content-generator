import base64

class Speech:
    '''Speech dictated by a character's voice'''

    def __init__(self, voice, speech):
        '''
        Constructs a new segment of speech
        Args:
            voice (Voice): Voice dictating the speech
            speech (dict): ElevenLabs API response speech model
        Returns:
            void
        '''
        
        self.text = ''.join(speech['alignment']['characters'])
        self.voice = voice
        self.character_start_times = speech['alignment']['character_start_times_seconds']
        self.character_end_times = speech['alignment']['character_end_times_seconds']
        
    
    def CompressToMp3(self):
        '''
        Decodes a base64 string into mp3 data
        Args: N/A
        Returns:
            byte string: byte string containing the mp3 data
        '''
        try:
            return base64.b64decode(self.audio_base64)
        except:
            raise ValueError('Unable to convert base64 string to mp3')
