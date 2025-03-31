SPEAKER_CHANGE = '/' # Char in script string that indicates speaker change

class Dialogue:
    '''A conversation between two characters'''
    
    def __init__(self, voice1, voice2, script):
        '''
        Constructs a new conversation
        Args:
            voice1 (voice): Voice of the first character
            voice2 (voice): Voice of the second character
            script (string): Script that the two characters follow in their
            speech
        Returns:
            void
        '''
        if (len(script) < 20 or len(script.split(SPEAKER_CHANGE)) < 2):
            raise ValueError('Unable to construct dialogue object due to invalid'
            ' script')
        
        self.voice1 = voice1
        self.voice2 = voice2
        self.script = script.split(SPEAKER_CHANGE)
        self.mp3_data = b""

    def CreateAllSpeech(self):
        '''
        Concatenates mp3 data of all conversation segments
        Args: N/A
        Returns:
            void
        '''
        current = self.voice1
        for line in self.script:
            self.mp3_data += current.CreateSpeech(line).CompressToMp3()
            # Flip voice
            if (current == self.voice1):
                current = self.voice2
            else:
                current = self.voice1

    def CreateMp3(self):
        '''
        Saves entire conversation's mp3data to a file
        Args: N/A
        Returns:
            void
        '''
        with open("./audio/convo.mp3", "wb") as mp3_file:
            mp3_file.write(self.mp3_data)
