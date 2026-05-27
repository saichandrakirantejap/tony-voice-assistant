"""
wiki.py

Wikipedia search for general knowledge questions.
Returns a short summary — 2 sentences is enough for a spoken response.
"""

import wikipedia


def search_wikipedia(query: str) -> str:
    """Search Wikipedia and return a 2-sentence summary."""
    if not query:
        return "What would you like to know about?"

    try:
        wikipedia.set_lang("en")
        result = wikipedia.summary(query, sentences=2)
        return result

    except wikipedia.exceptions.DisambiguationError as e:
        # Multiple results — pick the first one
        try:
            result = wikipedia.summary(e.options[0], sentences=2)
            return result
        except Exception:
            return f"I found multiple results for {query}. Can you be more specific?"

    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find anything about {query} on Wikipedia."

    except Exception:
        return "Sorry, I had trouble searching Wikipedia right now."
