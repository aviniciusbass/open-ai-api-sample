import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()

def get_response(messages):
    completation = client.chat.completions.create(
        messages=messages,
        model='gpt-3.5-turbo-0125',
        max_tokens=500,
        temperature=0,
        stream=True
    )

    print('Assistent: ', end='')
    message = ''
    for stream_completation in completation:
        if stream_completation.choices:
            token = stream_completation.choices[0].delta.content
            if token:
                print(token, end='')
                message += token

    print()
    messages.append({'role': 'assistant', 'content': message})
    return messages


if __name__ == '__main__':
    print('Bem Vindo ao Chatbot!')
    messages = []

    while True:
        input_text = input('User: ')

        if input_text == 'exit':
            break

        messages.append({'role': 'user', 'content': input_text})
        messages = get_response(messages)