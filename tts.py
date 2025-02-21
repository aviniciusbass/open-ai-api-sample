import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()

file = 'audios/python.mp3'
text = '''
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. Ela é amplamente usada para desenvolvimento web, automação, ciência de dados, inteligência artificial, desenvolvimento de jogos, entre outras aplicações.

Algumas características do Python:

Sintaxe Simples e Legível → Fácil de aprender e entender.
Multiparadigma → Suporta programação procedural, orientada a objetos e funcional.
Bibliotecas e Frameworks Poderosos → Possui uma grande variedade de pacotes como Flask, Django, Pandas, NumPy e TensorFlow.
Portabilidade → Funciona em diferentes sistemas operacionais como Windows, macOS e Linux.
Grande Comunidade → Muitas documentações, tutoriais e suporte da comunidade.
Você já teve contato com Python antes ou quer aprender do zero?
'''

response = client.audio.speech.create(
    model='tts-1',
    voice='onyx',
    input=text
)

response.write_to_file(file)