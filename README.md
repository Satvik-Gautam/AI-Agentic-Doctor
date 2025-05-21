# 🩺 AI Doctor with Vision and Voice

A cutting-edge AI- Agentic Application that leverages AI to provide medical insights based on voice input and optional medical image analysis. Built using Gradio for the interface, Groq for multimodal AI processing, and gTTS and elevenlabs for text-to-speech, this project simulates a virtual doctor consultation experience. Users can speak their symptoms, upload medical images (e.g., X-rays, skin conditions), and receive a professional, human-like response from an AI doctor, delivered both as text and audio. The application is hosted publicly on Hugging Face Spaces for easy access.

---

## 📖 Project Overview

The **AI Doctor with Vision and Voice** project creates an accessible, user-friendly platform where users can describe medical concerns via voice and optionally upload relevant medical images. The system transcribes the audio input, analyzes it alongside any provided images using a multimodal AI model, and generates a concise medical evaluation in the form of a doctor's response. The response is presented as text and converted to audio for an immersive experience, mimicking a real doctor-patient interaction. This project demonstrates the integration of speech recognition, computer vision, and natural language processing to deliver actionable medical insights in a professional and engaging manner.

### Objective
The primary objective is to provide a proof-of-concept for an AI-powered virtual doctor that can:
- Accept voice-based symptom descriptions from patients.
- Analyze medical images (if provided) for potential abnormalities.
- Deliver clear, professional, and concise medical advice in both text and audio formats.
- Make healthcare consultations more accessible and engaging using modern AI technologies.

### Features
- **Voice Input**: Record audio to describe symptoms, transcribed using Groq's Whisper model.
- **Image Analysis**: Upload medical images (e.g., X-rays, skin images) for AI-based evaluation.
- **Multimodal AI**: Combines text (transcribed symptoms) and image data for comprehensive analysis.
- **Text and Audio Output**: Receive the AI doctor's response as text and an auto-playing audio file for a human-like consultation experience.
- **User-Friendly Interface**: Built with Gradio, featuring a clean, responsive UI with custom CSS animations and gradients.
- **Error Handling**: Robust logging and error reporting for audio, image processing, and API interactions.
- **Public Hosting**: Deployed on Hugging Face Spaces for seamless access.
- **Cross-Platform Compatibility**: Modular code structure supports local deployment and various operating systems.

---

## 🚀 Project Flow

The project follows a streamlined workflow to process user inputs and generate medical insights:

1. **User Input Collection**:
   - **Audio Input**: Users record their symptoms via a microphone using the Gradio interface, saved as an MP3 file.
   - **Image Input (Optional)**: Users can upload a medical image (e.g., JPEG) for analysis, such as an X-ray or skin lesion.

2. **Audio Transcription**:
   - The recorded audio is transcribed into text using the `whisper-large-v3` model via the Groq API (`voice_of_the_patient.py`).
   - The transcription captures the user's spoken description of symptoms in English.

3. **Image Encoding**:
   - If an image is provided, it is converted to a base64-encoded string for compatibility with the AI model (`brain_of_doctor.py`).

4. **AI Analysis**:
   - The transcribed text and encoded image (if provided) are combined with a system prompt instructing the AI to act as a professional doctor.
   - The `meta-llama/llama-4-scout-17b-16e-instruct` model (via Groq API) analyzes the inputs and generates a concise medical evaluation, including potential diagnoses and recommendations (`brain_of_doctor.py`).

5. **Response Generation**:
   - The AI's text response is converted to an audio file using gTTS (Google Text-to-Speech) for a natural, spoken output (`voice_of_the_doctor.py`).
   - The audio is saved as an MP3 file and set to autoplay in the Gradio interface.

6. **Output Display**:
   - The Gradio interface displays:
     - The transcribed text of the user's audio input.
     - The AI doctor's text response.
     - The auto-playing audio of the doctor's response.
     - A status message indicating success or any errors during processing.

7. **Error Handling and Logging**:
   - Comprehensive logging is implemented across all modules to track the process and catch errors (e.g., audio recording failures, API issues).
   - Errors are displayed in the interface to inform the user of any issues.

---

## 🛠 Tech Stack and Technologies

The project integrates a variety of modern tools and libraries to achieve its functionality:

- **Python**: Core programming language for the application.
- **Gradio**: Creates a web-based interface with audio and image input components and a responsive, styled design.
- **Groq API**:
  - **whisper-large-v3**: High-accuracy speech-to-text transcription for user audio.
  - **meta-llama/llama-4-scout-17b-16e-instruct**: Multimodal model for analyzing text and images to generate medical insights.
- **gTTS (Google Text-to-Speech)**: Converts the AI's text response into a natural-sounding audio file.
- **SpeechRecognition**: Python library for capturing microphone input and handling audio data.
- **Pydub**: Processes and converts audio files (e.g., WAV to MP3).
- **Base64**: Encodes images into a format suitable for the Groq API.
- **python-dotenv**: Manages environment variables (e.g., API keys) for secure configuration.
- **Logging**: Built-in Python logging for debugging and monitoring.
- **Hugging Face Spaces**: Hosts the application publicly for easy access.
- **Custom CSS**: Enhances the Gradio interface with animations, gradients, and a professional aesthetic.

---

## 📂 Project Structure
- 📦 Project Root
 -  ├── 📄 app.py
     -   └─ Main application file with Gradio interface and core logic
 -  ├── 📄 brain_of_doctor.py
      -   └─ Handles image encoding and multimodal AI analysis
  - ├── 📄 voice_of_the_patient.py
      -   └─ Manages audio recording and speech-to-text transcription
  - ├── 📄 voice_of_the_doctor.py
      -    └─ Converts AI responses to audio using gTTS
  - ├── 📄 .env
      -    └─ Stores environment variables (e.g., API keys)
  - └── 📄 README.md
      -    └─ Project documentation (this file)

### File Descriptions
- **`app.py`**:
  - Defines the Gradio interface with custom CSS for styling.
  - Orchestrates the workflow by calling functions from other modules.
  - Handles input processing, error handling, and output rendering.
- **`brain_of_doctor.py`**:
  - Encodes images to base64 for API compatibility.
  - Uses the Groq API to analyze images and text with a multimodal model.
- **`voice_of_the_patient.py`**:
  - Records audio from the microphone and saves it as an MP3.
  - Transcribes audio to text using Groq's Whisper model.
- **`voice_of_the_doctor.py`**:
  - Converts the AI's text response to audio using gTTS.
  - Includes commented-out code for ElevenLabs TTS (alternative, not currently used).

---
### Prerequisites
- Python 3.8 or higher
- FFmpeg (for audio processing)
- PortAudio (for microphone input)
- A Groq API key (sign up at [console.groq.com](https://console.groq.com))
- The GitHub link [Github Repo Link](https://github.com/Satvik-Gautam/AI-Agentic-Doctor)

---
### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Satvik-Gautam/AI-Agentic-Doctor.git
   cd AI-Agentic-Doctor
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the Application**:
   ```bash
   python app.py

---
### Hugging Face Space
- Try the live demo of the AI Doctor application on Hugging Face Spaces: [HuggingFace Space Link](https://huggingface.co/spaces/SATVIKGAUTAM/AI-Doctor-with-Vision-and-Voice)

### 📝 Usage
- Access the Interface:
   - Open the application via the Hugging Face Space link or run it locally.
- Record Symptoms:
   - Click the microphone button in the Gradio interface to record a description of your symptoms.
- Speak clearly, e.g., "I have a rash on my arm that itches a lot."
- Upload an Image (Optional):
   -  Upload a medical image (e.g., a photo of a rash or an X-ray) using the image input field.
- Submit:
   - Click the "Submit" button to process your inputs.
- View Results:
   - The interface displays: Your transcribed symptoms (text).
- The AI doctor's written response with medical insights.
- An auto-playing audio of the doctor's response.
- Troubleshooting:
      - Check the logs in the terminal for any errors (e.g., API key issues, audio recording failures).
- Ensure FFmpeg and PortAudio are installed correctly.

### 🤝 Contributing
 - Contributions are welcome! To contribute:

   - Fork the repository.
   - Create a new branch (git checkout -b feature/your-feature).
   - Make your changes and commit (git commit -m "Add your feature").
   - Push to your branch (git push origin feature/your-feature).
   - Open a pull request on the GitHub repository.
### 📜 License
 - This project is licensed under the MIT License. See the LICENSE file for details.

### 🙏 Acknowledgments
- Groq: For providing the Whisper and Llama models via their API.
- Gradio: For the intuitive and customizable web interface.
- gTTS: For reliable text-to-speech conversion.
- Hugging Face: For hosting the application on Spaces.
- Open-Source Community: For libraries like SpeechRecognition and Pydub.

### 📫 Contact
- GitHub: [Satvik-Gautam](https://github.com/Satvik-Gautam?tab=repositories)
- LinkedIn: [Satvik Gautam](https://www.linkedin.com/in/gautamsatvik/)











