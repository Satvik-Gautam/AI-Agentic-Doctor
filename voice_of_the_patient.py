import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


logging.basicConfig(level=logging.INFO ,format='%(asctime)s - %(levelname)s - %(message)s') # To Prin the logs and show the level of logs getting and overall

#Step 1 Setup AUdio Recorder (ffmpeg and portaudio)
def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_limit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


#audio_file_path ="patient_voice_test.mp3" for testing only 
#record_audio(file_path=audio_file_path)

# Step 2: Setup the Speech to Text-SST-MODEL for transcription
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model ="whisper-large-v3"
def transcribe_with_groq(GROQ_API_KEY , stt_model , audio_file_path):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file =open(audio_file_path ,"rb")
    transcription = client.audio.transcriptions.create(
        model = stt_model,
        file = audio_file,
        language= "en"
    )
    return transcription.text