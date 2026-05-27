"""
commands.py

Intent matching and command routing.

Each command checks if certain keywords appear in the spoken text
and routes to the appropriate handler. Simple keyword matching
works well enough for the scope of this assistant — the goal was
reliability on common commands rather than handling every possible
phrasing.
"""

import webbrowser
import subprocess
import pyjokes
from weather import get_weather
from wiki import search_wikipedia
from utils import get_time, get_date


def handle_command(command: str) -> str:
    """
    Match the command text to an intent and return a response string.
    Returns empty string if no intent matched.
    """
    command = command.lower()

    # Time and date
    if "time" in command:
        return get_time()

    if "date" in command:
        return get_date()

    # Weather
    if "weather" in command:
        city = extract_city(command)
        return get_weather(city)

    # Wikipedia search
    if any(word in command for word in ["what is", "who is", "tell me about", "explain"]):
        query = (command
                 .replace("what is", "")
                 .replace("who is", "")
                 .replace("tell me about", "")
                 .replace("explain", "")
                 .strip())
        return search_wikipedia(query)

    # Web search
    if "search" in command or "google" in command:
        query = command.replace("search", "").replace("google", "").replace("for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}"

    # Open applications
    if "open browser" in command or "open chrome" in command:
        webbrowser.open("https://www.google.com")
        return "Opening browser"

    if "open notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening notepad"

    if "open calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening calculator"

    # Jokes
    if "joke" in command:
        return pyjokes.get_joke()

    # Identity
    if any(word in command for word in ["your name", "who are you", "what are you"]):
        return "I'm Tony, your voice assistant. I can answer questions, check the weather, tell jokes, and more."

    # No match
    return "I'm not sure how to help with that. Try asking about the weather, time, or a Wikipedia topic."


def extract_city(command: str) -> str:
    """Extract city name from weather commands."""
    for word in ["weather", "in", "for", "at"]:
        command = command.replace(word, "")
    city = command.strip()
    return city if city else "Birmingham"
