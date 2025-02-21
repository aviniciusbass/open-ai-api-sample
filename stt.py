import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()

audio = open('audios/python.mp3', 'rb')

response = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio,
    #prompt='posso passar algumas informacoes como nomes próprios, empresas e etc.',
    #response_format='srt',
    #language='pt'
)

print(response.text)