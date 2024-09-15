**Jarvis** is a sophisticated personal voice assistant built in Python, leveraging advanced libraries to provide seamless interactions and useful functionalities. From managing your daily tasks to entertaining you with jokes, Jarvis is designed to make your life easier and more enjoyable.

## Overview

Jarvis integrates multiple functionalities into one voice-controlled assistant. It can handle web searches, play music, send emails, provide weather updates, and more, all through simple voice commands. The assistant is built to be intuitive, interactive, and user-friendly, making it an ideal tool for both productivity and leisure.

Key Features

- **Personalized Greetings**: Welcomes you based on the time of day.
- **Wikipedia Search**: Fetches and summarizes Wikipedia articles.
- **Web Navigation**: Opens websites such as YouTube, Google, and StackOverflow.
- **Music Playback**: Plays music from a specified directory.
- **Time Telling**: Announces the current time.
- **Code Editor Launch**: Opens Visual Studio Code.
- **Email Functionality**: Sends emails via Gmail.
- **Joke Telling**: Shares random jokes for a bit of fun.
- **Weather Updates**: Provides current weather information (optional).
- **Exit Command**: Gracefully terminates the application.

## Tech Stack

- **Programming Language**: Python
- **Libraries**: 
  - `pyttsx3` (Text-to-Speech)
  - `speech_recognition` (Speech-to-Text)
  - `wikipedia` (Wikipedia API)
  - `webbrowser` (Web Navigation)
  - `os` (File Operations)
  - `smtplib` (Email)
  - `random` (Random Operations)
  - `sys` (System Operations)

## Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed.
2. **Required Libraries**: Install the necessary libraries using pip:

   ```bash
   pip install pyttsx3 speech_recognition wikipedia requests
   ```

3. **PyAudio**: Required for speech recognition, install it with:

   ```bash
   pip install pyaudio
   ```

4. **Email Credentials**: Configure your Gmail account for sending emails. Use an [App Password](https://support.google.com/accounts/answer/185833) for security.

5. **Weather API Key** (Optional): Obtain a free API key from a weather service like [OpenWeatherMap](https://openweathermap.org/).

## Configuration

1. **Customize User Name**: Edit the `user_name` variable to your preferred name.

2. **Update File Paths**:
   - **Music Directory**: Set the `music_dir` variable to your music directory path.
   - **VS Code Path**: Set the `codePath` variable to the path of your Visual Studio Code executable.

3. **Email Setup**:
   - Replace `'your-email@gmail.com'` with your Gmail address.
   - Replace `'your-app-password'` with your Gmail App Password.

4. **Weather API Key**: Replace `your-weather-api-key` and `your-city` in the `getWeather()` function with your actual API key and city.

## Usage

1. **Run the Program**: Execute the Python script to start Jarvis.

   ```bash
   python jar.py
   ```

2. **Interact with Jarvis**:
   - Speak commands like "open YouTube", "play music", or "what is the weather".
   - Use "exit" or "goodbye" to stop the program.


