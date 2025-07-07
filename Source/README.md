# AI-powered Transcription and Task Assignment System

## Overview
This project is an AI-powered transcription and task assignment system designed for businesses. It processes both audio files and live audio streams, transcribes them into text, and assigns tasks based on keywords or AI-based analysis.

## Features
- **Input Handling**: Accepts audio files and live audio streams.
- **Transcription**: Uses Gemini (open-source transcription model) fine-tuned for Malaysia accents and accounting jargon.
- **Task Assignment**: Implements keyword-based and AI-based analysis for task identification.
- **User Authentication**: Supports Google and Microsoft email authentication.
- **Integration**: Integrates with email systems for task notifications using SMTP.
- **Web Application**: Provides interfaces for uploading audio files, viewing transcriptions, and managing tasks.
- **Feedback Loop**: Allows users to improve transcription accuracy and task assignment logic.

## Technologies
- **Frontend**: React.js
- **Backend**: Flask (Python-based)
- **Audio Processing**: FFmpeg
- **Transcription**: Gemini
- **Task Assignment**: Custom Python logic
- **Authentication**: OAuth2 for Google and Microsoft email authentication
- **Email Integration**: SMTP
- **Deployment**: Azure App Service and Azure Functions

## Deployment
The system is deployed on Azure for Students (free tier) using Azure App Service for hosting the web app and Azure Functions for backend processing.

## Getting Started
1. Clone the repository.
2. Set up the development environment.
3. Follow the instructions in the `copilot-instructions.md` file for customization.

## License
This project is open-source and available under the MIT License.
