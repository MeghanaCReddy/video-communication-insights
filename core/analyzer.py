import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-2.5-flash"

def analyze_transcript(transcript: str) -> str:
    prompt = f"""
    You are an expert communication analyst. Analyze the following transcript strictly for **clarity** (how clearly ideas are expressed and understood).

    Transcript:
    {transcript}

    Provide your output in exactly this format:
    Clarity Score: [X]/10
    [Two-sentence description summarizing the main clarity strengths and weaknesses.]

    Do not include any headings, bullet points, or extra text.
    """

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)

    return response.text.strip()