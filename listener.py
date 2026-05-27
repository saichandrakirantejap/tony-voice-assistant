"""
listener.py

Microphone input and speech recognition using Google Speech API.

Google Speech API was chosen over offline recognition (CMU Sphinx)
because accuracy was noticeably better, especially on accented speech.
The assistant is meant to be used on a laptop with internet access
so the API round trip is acceptable.
"""

import speech_recognition as sr


recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000    # adjust based on microphone sensitivity
recognizer.pause_threshold = 0.8      # seconds of silence before phrase ends


def listen() -> str:
    """Listen for a command and return it as text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            print("Could not reach Google Speech API — check internet connection.")
            return ""


def listen_for_wake_word(wake_word: str = "tony") -> bool:
    """
    Listen continuously for the wake word.
    Returns True when wake word is detected.
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            text = recognizer.recognize_google(audio).lower()
            return wake_word in text
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            return False
