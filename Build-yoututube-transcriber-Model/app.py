import streamlit as st
from dotenv import load_dotenv
import os
from transcript import extract_transcript

load_dotenv()

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def fetch_transcript(video_id):
    transcript_text = extract_transcript(video_id)
    return transcript_text

def generate_notes(transcript_text, subject):
    # Your existing code for generating prompts based on the subject
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(subject + transcript_text)
    return response.text

def main():
    st.title("YouTube Transcript to Detailed Notes Converter")

    subject = st.selectbox("Select Subject:", ["Physics", "Chemistry", "Mathematics", "Data Science and Statistics"])
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if youtube_link:
        video_id = youtube_link.split("=")[-1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Get Detailed Notes"):
        # Call function to extract transcript
        transcript_text = extract_transcript(youtube_link)
        
        if transcript_text:
            st.success("Transcript extracted successfully!")
            # Generate detailed notes
            detailed_notes = generate_notes(transcript_text, subject)
            st.markdown("## Detailed Notes:")
            st.write(detailed_notes)
        else:
            st.error("Failed to extract transcript.")

if __name__ == "__main__":
    main()
