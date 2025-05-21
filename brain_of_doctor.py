# Setup the GROQ API KEY
import os
from dotenv import load_dotenv
load_dotenv()
GRQO_API_KEY = os.environ.get("GRQO_API_KEY")

# Step up the image as per required format is base64 convert's the  binary data to ASCII Code
import base64 



#image_path = "abc.jpg"
#Implementing the image encoding inside a function to be used in a export on
def encode_image(image_path):
    image_file = open(image_path ,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


#Step 3 setup Multimodel LLM
from groq import Groq
model ="meta-llama/llama-4-scout-17b-16e-instruct" # Llama  Image and Vision Model
# Implementing the Groq model inside a function to be imported 
def analyze_image_with_query(query , model , encoded_image):
    client = Groq()
    messages =[
        {
            "role":"user",
            "content": [
                {
                    "type":"text",
                    "text":query
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages= messages,
        model = model
    )

    return chat_completion.choices[0].message.content


