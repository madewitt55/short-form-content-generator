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
        
        self.characters = speech['alignment']['characters']
        self.voice = voice
        self.audio_base64 = speech['audio_base64']
        self.character_start_times = speech['alignment']['character_start_times_seconds']
        self.character_end_times = speech['alignment']['character_end_times_seconds']

    def GetWordDurations(self):
         '''
         Returns an array of dicts containing the word, start time, and end 
         time (seconds) for each word in the speech

         Args:
            None

        Returns:
            [dict]: Array of dicts with keys: text, start, and end
         '''
         words = []
         start = 0
         for i in range(len(self.characters) + 1):
             if (i == len(self.characters) or self.characters[i] == ' '):
                 words.append({
                     'text': ''.join(self.characters[start:i]),
                     'start': self.character_start_times[start],
                     'end': self.character_end_times[i-1]
                 })
                 start = i
         return words
    
    def CompressToMp3(self):
        '''
        Decodes a base64 string into mp3 data and returns it

        Args:
            None

        Returns:
            byte string: byte string containing the mp3 data
        '''
        try:
            return base64.b64decode(self.audio_base64)
        except:
            raise ValueError('Unable to convert base64 string to mp3')
