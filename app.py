import openai
import os
import gradio as gr


openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = []
messages.append({'role': 'system', 'content': 'you are the CTO of the largest company in the world, you speak like a 70s gangster'})

def respond(chat_history, msg):
    
    messages.append({'role': 'user', 'content': msg})
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
    messages.append(response.choices[0].message)

    response_text = str(response.choices[0].message.content)
    
    return chat_history + [[msg, response_text]]

with gr.Blocks() as my_app:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()

    msg.submit(respond, [chatbot, msg], chatbot)
    # add clear button https://gradio.app/creating-a-chatbot/

my_app.launch(share=True)
