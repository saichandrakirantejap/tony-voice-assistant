# Tony — Voice Assistant

A voice assistant built during my final year of BTech (ECE) at Sastra Deemed University. Named Tony. Runs on a laptop with a microphone — no special hardware required.

The goal was to build something that actually worked in daily use: wake up, listen, understand what was asked, respond in natural speech, and handle the most common tasks a student would need.

---

## What Tony Can Do

- **Answer general questions** — via Wikipedia
- **Tell the time and date** — instantly
- **Get weather** — current conditions for any city via OpenWeatherMap
- **Open applications** — browser, calculator, notepad
- **Tell jokes** — via pyjokes
- **Search the web** — opens Google search for any query
- **Greet based on time of day** — good morning / afternoon / evening
- **Respond to "who are you"** — knows its name and purpose

---

## How It Works

```
Microphone input
      │
      ▼
SpeechRecognition (Google Speech API)
      │  converts audio to text
      ▼
Intent Parser
      │  matches text to a command
      ▼
Command Handler
      │  Wikipedia / OpenWeatherMap / system calls
      ▼
pyttsx3 (text to speech)
      │  speaks the response aloud
      ▼
Speaker output
```

---

## Why I Built It This Way

**Google Speech API over offline recognition (CMU Sphinx):**
Offline recognition was noticeably less accurate, especially on accented speech. Since the laptop had internet access during normal use, Google Speech API gave much better results for the same effort.

**pyttsx3 over gTTS:**
pyttsx3 works offline and responds instantly — no round trip to Google's TTS server. For a voice assistant where response latency matters, this was the better choice.

**Wikipedia for general questions:**
For a BTech project the scope was realistic — answering factual questions well beats trying to answer everything poorly. Wikipedia covers most of what a student would actually ask.

---

## Repo Structure

```
tony-voice-assistant/
├── src/
│   ├── tony.py             # Main assistant loop
│   ├── listener.py         # Microphone input + speech recognition
│   ├── speaker.py          # pyttsx3 text to speech
│   ├── commands.py         # Intent matching and command routing
│   ├── weather.py          # OpenWeatherMap integration
│   ├── wiki.py             # Wikipedia search
│   └── utils.py            # Time, date, greetings
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup

```bash
git clone https://github.com/saichandrakirantejap/tony-voice-assistant
cd tony-voice-assistant
pip install -r requirements.txt
cp .env.example .env
# Add your OpenWeatherMap API key in .env
python src/tony.py
```

Then say **"Hey Tony"** to wake it up.

---

## Example Commands

```
"Hey Tony, what time is it?"
"Hey Tony, what is the weather in Birmingham?"
"Hey Tony, tell me about machine learning"
"Hey Tony, open the browser"
"Hey Tony, tell me a joke"
"Hey Tony, search for data science jobs"
```

---

## Stack

| Purpose | Tool |
|---|---|
| Speech recognition | SpeechRecognition + Google Speech API |
| Text to speech | pyttsx3 |
| General knowledge | Wikipedia API |
| Weather | OpenWeatherMap API |
| Jokes | pyjokes |
| Web search | webbrowser module |
| Language | Python 3 |

---

## About

Built as a final year project during BTech in Electronics and Communication Engineering at Sastra Deemed University, Thanjavur, Tamil Nadu, India (2018–2022). The goal was to build a functional voice-controlled assistant that runs entirely on a standard laptop with no additional hardware.

[LinkedIn](https://linkedin.com/in/saichandrapodili) · [Email](mailto:saichandrakirantejap@gmail.com)
