import gradio as gr
import os
from dotenv import load_dotenv
load_dotenv()


from brain_of_doctor import encode_image , analyze_image_with_query
from voice_of_the_patient import record_audio , transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts , text_to_speech_with_elevenlabs

# Providing a System Prompt to make it understand that it is a doctor 
system_prompt = """As a professional doctor, please evaluate the provided image for any medical abnormalities based on your expertise.
Describe any potential issues you observe, provide a differential diagnosis, and suggest appropriate remedies or next steps for management, 
addressing me directly as the patient in a clear and concise manner. 
Keep your response in a single paragraph, in max 3 sentence starting directly with your assessment (e.g., "Based on what I see, I suspect..."). 
Avoid using numbers, special characters, or phrases like "in the image," and maintain a professional, 
human-like tone as if speaking to a real patient, without referencing AI or technology.
"""

def process_inputs(audio_file_path, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_file_path=audio_file_path,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor
    


# Gradio OUTPUT Frontend 
custom_css = """
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #e6f0fa 0%, #d4e4f7 100%); /* Soft blue gradient background */
}
.gradio-container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}
h1 {
    color: #2b6cb0; /* Deep blue for title */
    text-align: center;
    font-size: 2.2em;
    animation: fadeIn 1s ease-in-out;
}
.input-container {
    background-color: #f1f9ff; /* Light blue for input area */
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
}
.output-container {
    background-color: #f0fff4; /* Light green for output area */
    padding: 15px;
    border-radius: 8px;
    animation: slideIn 0.5s ease-out;
}
.submit-btn {
    background: linear-gradient(45deg, #2b6cb0, #4299e1) !important; /* Gradient blue button */
    color: white !important;
    border-radius: 8px;
    padding: 12px 20px;
    transition: transform 0.2s, box-shadow 0.2s;
}
.submit-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.clear-btn {
    background: linear-gradient(45deg, #e53e3e, #f56565) !important; /* Gradient red button */
    color: white !important;
    border-radius: 8px;
    padding: 12px 20px;
    transition: transform 0.2s, box-shadow 0.2s;
}
.clear-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.textbox {
    border: 2px solid #90cdf4 !important; /* Light blue border for textboxes */
    border-radius: 6px;
    transition: border-color 0.3s;
}
.textbox:focus {
    border-color: #2b6cb0 !important; /* Darker blue on focus */
}
.audio-output {
    border: 2px solid #68d391 !important; /* Green border for audio output */
    border-radius: 6px;
}
.description-text {
    color: #1a5f6f; /* Dark teal for the description text */
    font-size: 1.1em;
    text-align: center;
    animation: fadeIn 1.5s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes slideIn {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
"""

# Build the enhanced interface with Blocks to match gr.Interface structure
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="green"), css=custom_css) as demo:
    gr.Markdown(
        """
        # 🩺 AI Doctor with Vision and Voice
        <div class="description-text">Speak or upload an image to consult with our AI doctor. Your voice will be transcribed, and the doctor will analyze any provided image to offer medical insights.</div>
        """,
        elem_classes="fadeIn"
    )

    # Input section
    with gr.Group(elem_classes="input-container"):
        audio_input = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Speech to Text"
        )
        image_input = gr.Image(
            type="filepath",
            label="Medical Image (Optional)"
        )

    # Submit button
    submit_btn = gr.Button("Submit", variant="primary", elem_classes="submit-btn")

    # Output section
    with gr.Group(elem_classes="output-container"):
        speech_output = gr.Textbox(label="Speech to Text", elem_classes="textbox")
        doctor_response = gr.Textbox(label="Doctor's Response", elem_classes="textbox")
        audio_output = gr.Audio(label="Doctor's Response (Audio)", value="final.mp3", elem_classes="audio-output")

    # Event listener for submit button
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[speech_output, doctor_response, audio_output],
        show_progress="full"  # Add loading animation
    )

# Launch the app
demo.launch(share=True)