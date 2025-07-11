#modules to download
#pip install gradio google-generativeai
#pip install google-generativeai

from dotenv import load_dotenv
import gradio as gr
import google.generativeai as genai
import os

load_dotenv("keys.env")
api= os.getenv("chatbot")

genai.configure(api_key=api)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
chat = model.start_chat(history=[])



def chat_with_gemini(message, history):
    history = history or []
    response = chat.send_message(message)
    history.append(("🧑 You: " + message, "🤖 :   " + response.text.strip()))
    return history, history,""



with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🤖 The Ultimate Chatbot
    Welcome! Lets have some Chit Chat.
    """)

    chatbot = gr.Chatbot(label="Chat", bubble_full_width=False)
    msg = gr.Textbox(placeholder="Type your message...", show_label=False)
    clear = gr.Button("🧹 Clear Chat")

    state = gr.State([])

    msg.submit(chat_with_gemini, [msg, state], [chatbot, state, msg])
    clear.click(lambda: ([], []), None, [chatbot, state])

demo.launch()
