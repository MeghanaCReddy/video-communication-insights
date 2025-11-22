import streamlit as st
from core.extractor import download_and_extract_audio, extract_audio
from core.transcriber import transcribe_audio
from core.analyzer import analyze_transcript
import os

st.set_page_config(page_title="Video Communication Insights", layout="wide")

st.title("Video Communication Insights")
st.write("Upload a video or paste a YouTube link to analyze communication clarity.")

upload_type = st.radio("Select Input Type:", ["Upload Video", "YouTube URL"])

audio_path = None

os.makedirs("downloads", exist_ok=True)

if upload_type == "Upload Video":
    uploaded_file = st.file_uploader("Upload MP4, MOV, or MKV", type=["mp4", "mov", "mkv"])

    if uploaded_file:
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.read())

        st.success("Video uploaded successfully!")
        st.write("Extracting audio...")

        audio_path = extract_audio("temp_video.mp4", "downloads/audio.wav")

else:
    youtube_url = st.text_input("Enter YouTube URL")

    if youtube_url and st.button("Process YouTube Video"):
        st.write("Downloading & extracting audio… please wait.")
        audio_path = download_and_extract_audio(youtube_url, "downloads")

if audio_path:
    st.audio(audio_path)
    st.success("Audio extracted successfully!")

    st.write("Transcribing audio…")
    transcript = transcribe_audio(audio_path)

    if not transcript:
        st.error("Transcription failed. Check logs.")
        st.stop()

    st.success("Transcription completed!")

    st.subheader("Transcript")
    st.write(transcript)

    st.subheader("Communication Analysis")

    with st.spinner("Analyzing using Google Gemini…"):
        analysis_text = analyze_transcript(transcript)

    st.write(analysis_text)

    st.success("Analysis completed!")
