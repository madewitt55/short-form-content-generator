# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-03-28

### Added
- Functionality to retrieve all cloned voices from ElevenLabs API

## [0.1.1] - 2025-03-30

### Added
- Uncompleted Voice class
- character_qualities.py to store user inputted information on their characters
(currently untracked)
- audio folder for mp3 outputs
- Functionality to submit a text-to-speech request to ElevenLabs
- Functionality to convert a base64 string to an mp3 file

### Changed
- Changed request error handling to raise an HTTPError rather than
a generic Exception

## [0.2.0] - 2025-03-31

### Added
- Speech class
- Dialogue (conversation) class
- Additional error handling in multiple files
- elevenlabs.py file to hold the API base url and default headers

### Changed
- Moved functionality for submitting a TTS request to voice class, which in turn
creates a speech object with the response data
- Moved functionality to convert a base64 string to mp3 to speech class, and changed it
so it returns the compress mp3 data rather than saving it to a file
- Moved functionality to save mp3 to a file to dialogue class (this happens after
combining multiple sources of mp3 data to form a conversation between two characters)

### Removed
- GenerateException function
- character_qualities.py, because it is currently unused and I will replace it
with a JSON file when it is needed

## [0.3.0] - 2025-04-01

### Added
- Added members audio_base64, character_start_times_seconds,
character_end_times_seconds to speech class
- Added member function GetWordDurations to speech class, used to get
any and all caption data
- Video class (using moviepy), which overlays the mp3 audio over a randomly 
selected background video from background_videos folder
- Video class saves both the mp3 and mp4 files to a new folder inside the videos
folder
- Settings.json, a file to set basic settings for the application; currently it
has font, font-size, use-captions, caption-style

### Changed
- Minor changes to dialogue class

### Removed
- Audio folder (previously untracked)

## [0.3.1] - 2025-04-02

### Changed
- GetVoices function to return elevenlabs response data rather than creating
an object for each voice
- Commented out unfinished block to add character images to video in Video class

### Added
- Select menu for selecting the two voices for the script
- character_settings.json for setting custom names and image paths for voices
using their voice id (printed during the menu). More settings will come to this
file in the future
- character_images folder for storing character images