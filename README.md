## 🎙️ Desktop voice assistant

## 🌟 Overview

The Voice Assistant Project is a Python-based desktop application designed to provide a variety of functionalities through voice commands. This virtual assistant can perform tasks such as telling the time and date, telling jokes, searching Wikipedia, and more.

## 📌Built with

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## 🚀 Features

- **Voice Commands**: Interact with the assistant using voice commands.
- **Time and Date**: Retrieve the current time and date.
- **Jokes**: Hear random jokes to lighten up your mood.
- **Wikipedia Search**: Search Wikipedia and receive a summary of articles.
- **Web Browsing**: Open websites such as YouTube, Google, and Stack Overflow.
- **Media Control**: Play music from a specified directory.
- **Screenshot Capture**: Take and save screenshots.
- **Memory**: Save and recall user-provided information.
- **Translation**: Translate text into different languages.

 ## Requirements 📋

- To run the Voice Assistant Project, you need to have the following software and libraries installed:

### Software Requirements 🖥️

- **Python**: Version 3.6 or higher is required. Python is the programming language used for the project.
  - [Download Python](https://www.python.org/downloads/)

- **Operating System**: The project is designed to run on Windows, but it can be adapted to other operating systems with minor modifications.


## 📌 Modules and Libraries Used

This project utilizes several Python libraries to achieve its functionality:

- **`pyttsx3`**: A text-to-speech conversion library in Python. It allows the assistant to speak responses to the user.
  - [Documentation](https://pyttsx3.readthedocs.io/)
  
- **`datetime`**: Provides classes for manipulating dates and times. Used to get the current date and time.
  - [Documentation](https://docs.python.org/3/library/datetime.html)

- **`speech_recognition`**: Recognizes speech and converts it into text. Enables voice command recognition.
  - [Documentation](https://pypi.org/project/SpeechRecognition/)
  
- **`wikipediaapi`**: A Python wrapper for the Wikipedia API. Allows the assistant to search and retrieve Wikipedia summaries.
  - [Documentation](https://wikipedia-api.readthedocs.io/en/latest/)
  
- **`webbrowser`**: A module to open URLs in a browser. Used to open websites.
  - [Documentation](https://docs.python.org/3/library/webbrowser.html)
  
- **`os`**: Provides a way of using operating system-dependent functionality like reading or writing to the file system.
  - [Documentation](https://docs.python.org/3/library/os.html)
  
- **`random`**: Implements pseudo-random number generators. Used to select random jokes and songs.
  - [Documentation](https://docs.python.org/3/library/random.html)
  
- **`pyautogui`**: Provides functions to control the mouse and keyboard. Used to take screenshots.
  - [Documentation](https://pyautogui.readthedocs.io/en/latest/)
  
- **`googletrans`**: A library for translating text using Google Translate API. Allows translation of text into different languages.
  - [Documentation](https://py-googletrans.readthedocs.io/en/latest/)

## Installation 🚀

To set up the Voice Assistant Project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <URL>
   cd desktop-voice-assistant

2. **Set up virtual environment**:
     - For Windows:
       ```bash
       python -m venv .venv  

       ```
     - For macOS/Linux:
       ```bash
       python3 -m venv .venv

3. **Activate the virtual environment**:
     - For Windows:
       ```bash
       .venv\Scripts\activate
       ```
     - For macOS/Linux:
       ```bash
       source .venv/bin/activate


4. **Install Requirements**

   - Install all the requirements given in **[requirements.txt](https://github.com/Sudiksha-16/Desktop-voice-assistant/blob/main/requirements.txt)** by running the command `pip install -r requirements.txt`

5.  **Run the Project**
  - Run the main script:
    ```bash
    python assistant.py
    ```

