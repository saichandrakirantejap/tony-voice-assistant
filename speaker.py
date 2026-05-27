"""
speaker.py

Text to speech using pyttsx3.

pyttsx3 works offline and responds instantly — no round trip to
a TTS server. For a voice assistant where response latency matters,
this was the better choice over gTTS which requires internet and
has noticeable delay.
"""

import pyttsx3


engine = pyttsx3.init()

# Voice settings
engine.setProperty("rate", 175)      # speaking speed
engine.setProperty("volume", 0.9)    # volume level

# Use a male voice if available
voices = engine.getProperty("voices")
for voice in voices:
    if "male" in voice.name.lower() or "david" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break


def speak(text: str) -> None:
    """Convert text to speech and play it."""
    print(f"Tony: {text}")
    engine.say(text)
    engine.runAndWait()
