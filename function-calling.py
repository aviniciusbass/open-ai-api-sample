import json
import openai
from dotenv import load_dotenv, find_dotenv

def get_temperature(locale, unit='celsius'):
    if 'são paulo' in locale.lower():
        return json.dumps({'locale': 'São Paulo', 'temperature': 25, 'unit': unit}, ensure_ascii=False)
    elif 'rio de janeiro' in locale.lower():
        return json.dumps({'locale': 'Rio de Janeiro', 'temperature': 30, 'unit': unit}, ensure_ascii=False)
    else:
        return json.dumps({'locale': locale, 'temperature': 'unknown'}, ensure_ascii=False)
    

load_dotenv(find_dotenv())
client = openai.Client()

tools = [   
    {
        'type': 'function',
        'function': {
            'name': 'get_temperature',
            'description': 'Obtém a temperatura atual de uma cidade',
            'parameters': {
                'type': 'object',
                'properties': {
                    'locale': {
                        'type': 'string',
                        'description': 'O nome da cidade. Ex: São Paulo'
                    },
                    'unit': {
                        'type': 'string',
                        'enum': ['celsius', 'fahrenheit'],
                    }
                },
                'required': ['locale']
            }
        }
    }
]

functions = { 'get_temperature': get_temperature }
messages = [
    { 'role': 'user', 'content': 'Qual a temperatura em São Paulo e Rio de Janeiro?' }
]

completion_1 = client.chat.completions.create(
    messages=messages,
    model='gpt-3.5-turbo-0125',
    tools=tools
)

message = completion_1.choices[0].message
tool_calls = message.tool_calls

if tool_calls:
    messages.append(message)
    for tool_call in tool_calls:
        func_name = tool_call.function.name
        func_to_call = functions[func_name]
        func_args = json.loads(tool_call.function.arguments)
        func_response = func_to_call(
            locale=func_args.get('locale'),
            unit=func_args.get('unit')
        )

        messages.append({
            'tool_call_id': tool_call.id,
            'role': 'tool',
            'name': func_name,
            'content': func_response
        })
    

completion_2 = client.chat.completions.create(
    model='gpt-3.5-turbo-0125',
    messages=messages,
    tools=tools
)

print(completion_2.choices[0].message.content)