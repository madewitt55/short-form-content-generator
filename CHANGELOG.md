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