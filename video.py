from moviepy.editor import (
    VideoFileClip, 
    AudioFileClip, 
    TextClip, 
    ImageClip, 
    CompositeVideoClip)
from moviepy.video.fx.resize import resize
import random
import os
import json

# Import settings from settings.json
with open("settings.json", "r") as file:
    settings = json.load(file)

class Video:
    def __init__(self, title, dialogue):
        '''
        Constructs a new video

        Args:
            title (string): Title of the video
            dialogue (Dialogue): Dialogue object that is the base of the video
        '''

        self.title = title
        self.folder_path = f'./videos/{title}'
        if (os.path.exists(os.path.join(os.getcwd(), self.folder_path))):
            raise ValueError(f'Video with title {title} already exists')  
        os.mkdir(self.folder_path)

        self.dialogue = dialogue
        self.dialogue.CreateMp3(os.path.join(self.folder_path, f'{title}.mp3'))
        self.audio = AudioFileClip(os.path.join(self.folder_path, f'{title}.mp3'))

        # Chooses random background video from background_videos folder
        self.video = VideoFileClip(os.path.join('./background_videos',
            random.choice(os.listdir('./background_videos'))))
        
        self.CompileVideo()
        self.SaveVideo(os.path.join(self.folder_path, f'{self.title}.mp4'))
        
    def CompileVideo(self):
        '''
        Overlays audio onto background video, and optionally burns captions and
        displays character images

        Args:
            None

        Returns:
            void
        '''

        self.video = self.video.set_audio(self.audio) # Overlay audio
        self.video = self.video.subclip(0, self.audio.duration) # Trim video to length of audio

        captions = []
        images = []
        if (settings['use-images']):
            current_voice = 0
            position = (self.dialogue.voices[current_voice].image_position, 'bottom')
            for speech in self.dialogue.speech_lines:
                timing = speech.GetWordDurations()
                image = (ImageClip(self.dialogue.voices[current_voice].image_path)
                    .set_duration(timing[-1]['end'] - timing[0]['start'])
                    .set_start(timing[0]['start']) 
                    .set_position((position))
                    .resize(width = 0.6 * self.video.size[0])
                )
                images.append(image)
                
                # Flip voice (character)
                current_voice = current_voice ^ 1
                position = (self.dialogue.voices[current_voice].image_position, 'bottom')

        if (settings['use-captions']):
            for speech in self.dialogue.speech_lines:
                for word in speech.GetWordDurations():
                    caption = TextClip(word['word'].upper(), 
                        fontsize=settings['font-size'], 
                        color="white", 
                        font=settings['font'])\
                    .set_position('center')\
                    .set_start(word['start'])\
                    .set_duration(word['end'] - word['start'])
                    captions.append(caption)
        
        self.video = CompositeVideoClip([self.video] + images + captions)

    def SaveVideo(self, output_path):
        '''
        Saves the video as an mp4 file at the specifed path

        Args:
            output_path (string): Where the file will be saved
            
        Returns:
            void
        '''
        self.video.write_videofile(output_path)
