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