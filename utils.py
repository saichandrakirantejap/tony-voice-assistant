"""
utils.py

Time, date, and greeting utilities.
"""

from datetime import datetime


def get_time() -> str:
    now = datetime.now()
    return f"The time is {now.strftime('%I:%M %p')}."


def get_date() -> str:
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."


def get_greeting() -> str:
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"
