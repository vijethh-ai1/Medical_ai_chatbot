#Step1: Setup GROQ API key
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step1: Setup GROQ API key
import base64

#image_path="acne.jpg"

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


#Step3: Setup Multimodal LLM 
from groq import Groq

query="Is there something wrong with my face?"
model="llama3-70b-8192"

def analyze_image_with_query(query, model, encoded_image):
  client = Groq(api_key="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")


  messages = [
    {"role": "user", "content": query}
  ]


  chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
  )

  return chat_completion.choices[0].message.content
