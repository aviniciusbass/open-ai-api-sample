import openai
import time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


#assistant = client.beta.assistants.create(
#    name="AKT Bot",
#    instructions="Você é um especialista em Trade Marketing",
#    model='gpt-4o'  
#)

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content='O que é vc?'
)

run = client.beta.threads.runs.create(
    assistant_id='asst_QsrJ8fouzWDR2PyBanl4u2lP',
    thread_id=thread.id
)

while run.status in ['cancelling', 'in_progress', 'queued']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    runs_steps = client.beta.threads.runs.steps.list(
        thread_id=thread.id,
        run_id=run.id
    )

    for step in runs_steps.data:
        print(f'{step.id}: {step.step_details.type}')

print()
if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    for message in messages:
        print(f'{message.role}: {message.content}')
