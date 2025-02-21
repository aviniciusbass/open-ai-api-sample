import requests
from PIL import Image

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()



response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'user', 
                'content': [
                    {'type': 'text', 'text': 'Descreva a imagem fornecida'},
                    {'type': 'image_url', 'image_url': {'url':  'https://firebasestorage.googleapis.com/v0/b/aktpdvus-dinamica.appspot.com/o/images%2F196229ff909fee443480e0f35bfb9a17.jpg?alt=media&token=2385c029-0cac-46a5-ae6a-02b4d6edcd76'}}
                ]
            }]
)

print(response.choices[0].message.content)