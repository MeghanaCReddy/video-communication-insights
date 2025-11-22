Video Communication Insights
Understand how clearly you (or anyone) communicates — from any video or YouTube link. 

This tool transcribes spoken content and uses AI to give you a clarity score and concise feedback—so you can speak with more impact, confidence, and precision.

Features
Upload any video (MP4, MOV, MKV) or paste a YouTube URL
Extract audio automatically
Transcribe speech locally using Meta’s Whisper (no cloud needed)
Get an instant Clarity Score (0–10) from Google’s Gemini 2.5 Flash
Receive a 2-sentence expert summary of communication strengths & weaknesses
Privacy-first: Transcription runs on your machine; only text (not audio) is sent to AI

Project Structure
video-comm-insights/
│
├── core/
│   ├── extractor.py      # Downloads YouTube videos & extracts audio (MP4 → WAV)
│   ├── transcriber.py    # Transcribes audio using Whisper (base model)
│   └── analyzer.py       # Sends transcript to Gemini for clarity scoring
│
├── downloads/            # Auto-created temporary folder for audio files
├── app.py                # Main Streamlit web app
├── requirements.txt      # Python dependencies
├── .env                  # Your Gemini API key (private!)
└── README.md

Getting Started
1. Clone the repository
git clone https://github.com/MeghanaCReddy/video-communication-insights.git
cd video-communication-insights
2. Create a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Set up your Gemini API key
    1. Go to Google AI Studio
    2. Create or copy your API Key
    3. Create a .env file in the project root
        GEMINI_API_KEY=your_actual_api_key_here
5. Launch the app
streamlit run app.py

Tech Stack
Frontend: Streamlit – beautiful, simple web UI in Python
Audio Extraction: pytubefix + pydub
Transcription: Whisper (base) – runs locally
AI Analysis: Google Gemini 2.5 Flash – fast, powerful, multimodal LLM
Backend: Pure Python – no servers, no databases

Limitations & Tips
Whisper base model works best for clear English audio. For higher accuracy (and slower speed), try small or medium in transcriber.py.
Gemini usage is low-cost, but not free at scale. Monitor usage in Google Cloud Console .
YouTube videos may fail if blocked by region or require login (e.g., age-restricted content).
The app stores temporary files in downloads/ — feel free to delete them after use.

Credits
Built with gratitude for:
Google Gemini
OpenAI Whisper
Streamlit
pytubefix – for reliable YouTube downloads

License
MIT License – use, modify, and share freely!