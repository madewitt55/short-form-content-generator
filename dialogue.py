SPEAKER_CHANGE = '/' # Char in script string that indicates speaker change

class Dialogue:
    '''A conversation between two characters'''
    
    def __init__(self, voices, script):
        '''
        Constructs a new conversation
        Args:
            voices [Voice]: Array of two voices whom will read the script
            script (string): Script that the two characters follow in their
            speech
        Returns:
            void
        '''
        if (len(script) < 20 or len(script.split(SPEAKER_CHANGE)) < 2):
            raise ValueError('Unable to construct dialogue object due to invalid'
            ' script')
        
        self.voices = voices
        self.script = script.split(SPEAKER_CHANGE)
        
        self.CreateAllSpeech() # Create speech objects for each line

    def CreateAllSpeech(self):
        '''
        Concatenates mp3 data of all conversation segments
        Args: N/A
        Returns:
            void
        '''
        
        self.speech_lines = []
        current_voice = 0

        # Create and store speech object for each line
        for line in self.script:
            speech = self.voices[current_voice].CreateSpeech(line)
            # Increment character time values to come after all previous clips
            # This is used for caption timing
            if (len(self.speech_lines)):
                offset = float(self.speech_lines[-1].character_end_times[-1])
                for i in range(len(speech.character_start_times)):
                    speech.character_start_times[i] += offset
                    speech.character_end_times[i] += offset
                    
            self.speech_lines.append(speech)
            
            # Flip voice
            current_voice = current_voice ^ 1

    def CreateMp3(self, output_path):
        '''
        Saves entire conversation's mp3 data to a file
        Args:
            output_path (string): Where mp3 file will be saved
        Returns:
            void
        '''

        mp3_data = b""
        for speech in self.speech_lines:
            mp3_data += speech.CompressToMp3()
        with open(output_path, "wb") as mp3_file:
            mp3_file.write(mp3_data)
