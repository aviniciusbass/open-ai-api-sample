import requests
from PIL import Image

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()



response = client.images.generate(
  model='dall-e-3',
  prompt='um copo de café em uma cafeteria nerd, com um quadro do homem de ferro ao fundo igual do filme vingadores',
  size='1024x1024',
  quality='hd',
  style='vivid',
  n=1
)

filename = 'images/image.jpg'
url = response.data[0].url
image = requests.get(url).content
with open(filename, 'wb') as file:
    file.write(image)

image = Image.open(filename)
image.show()