import gradio as gr
import ollama

MODEL_NAME = "llama2"
conversation = []

def get_reply(user_message, history):
    conversation.append({"role": "user", "content": user_message})

    response = ollama.chat(
        model=MODEL_NAME,
        messages=conversation,
        stream=False
    )

    reply = response["message"]["content"].strip()
    conversation.append({"role": "assistant", "content": reply})
    history.append((user_message, reply))
    return "", history

with gr.Blocks(title="🧠 Ollama Chatbot") as demo:
    gr.Markdown("### 🧠 Chat with Local Ollama (LLaMA2)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your message")
    clear_btn = gr.Button("Clear")

    msg.submit(get_reply, [msg, chatbot], [msg, chatbot])
    clear_btn.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.launch(inbrowser=True)
