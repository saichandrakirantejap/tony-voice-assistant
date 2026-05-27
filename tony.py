"""
tony.py

Main assistant loop for Tony.

Listens continuously for the wake word "tony" then
processes the command that follows. Responds via speech.
"""

import time
from listener import listen, listen_for_wake_word
from speaker import speak
from commands import handle_command
from utils import get_greeting


def run():
    speak(f"{get_greeting()}, I'm Tony. How can I help you?")

    while True:
        print("Listening for wake word...")
        wake = listen_for_wake_word()

        if wake:
            speak("Yes?")
            command = listen()

            if command:
                print(f"Command: {command}")

                # Exit commands
                if any(word in command.lower() for word in ["bye", "exit", "quit", "goodbye"]):
                    speak("Goodbye! Have a great day.")
                    break

                response = handle_command(command)
                if response:
                    speak(response)
            else:
                speak("Sorry, I didn't catch that.")

        time.sleep(0.5)


if __name__ == "__main__":
    run()
