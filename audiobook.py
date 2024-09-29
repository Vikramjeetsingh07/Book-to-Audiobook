import os
import re
import streamlit as st
import pyttsx3
import fitz  # PyMuPDF
from pathlib import Path  # Ensure this import is included

def extracting_pdf(pdf_file):
    # Open the PDF directly from the BytesIO object
    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")  # Read from the BytesIO stream
    text = ''
    for page in pdf:
        text += page.get_text()
    pdf.close()  # Don't forget to close the PDF after reading
    return text

def text_to_speech(texts, output_file, voice='male'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)

    voices = engine.getProperty('voices')
    if voice == 'male':
        engine.setProperty('voice', voices[0].id)
    elif voice == 'female':
        engine.setProperty('voice', voices[1].id)

    engine.save_to_file(texts, output_file)
    engine.runAndWait()

def fixing_filename(filename):
    filename = re.sub(r'[^\w\s-]', '', filename).strip().lower()
    return re.sub(r'[-\s]+', '-', filename)

st.title("PDF to Audiobook")
st.markdown("Generate an audiobook from PDF")

uploaded_pdf = st.file_uploader("Upload PDF here", type="pdf")
voice_choice = st.radio("Select narration voice", ('Male', 'Female'))

if uploaded_pdf is not None:
    pdf_filename = uploaded_pdf.name
    fixed_name = fixing_filename(Path(pdf_filename).stem)
    output_mp3_filename = f"{fixed_name}.mp3"

    if st.button("Generate Audiobook"):
        with st.spinner("Conversion under process..."):
            text = extracting_pdf(uploaded_pdf)  # Now reads from the BytesIO object correctly
            text_to_speech(text, output_mp3_filename, voice_choice.lower())

            if Path(output_mp3_filename).exists() and os.path.getsize(output_mp3_filename) > 0:
                st.success(f"Audiobook '{output_mp3_filename}' generated successfully!")
                st.audio(output_mp3_filename, format='audio/mp3')
                with open(output_mp3_filename, "rb") as file:
                    st.download_button(
                        label="Download Audiobook",
                        data=file,
                        file_name=output_mp3_filename,
                        mime="audio/mpeg"
                    )
            else:
                st.error("Failed to generate audiobook.")
