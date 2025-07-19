
import ollama

MODEL_NAME = "llama2"        # <<-- change to "mistral", "zephyr", etc. if you like


def get_reply(user_message: str, history: list[dict]) -> str:
    """
    history is a list of messages like:
    [{"role": "user", "content": "hi"}, {"role": "assistant", "content": "hello"}]
    """
    history.append({"role": "user", "content": user_message})

    response = ollama.chat(
        model=MODEL_NAME,
        messages=history,
        stream=False           # set True for token‑streaming
    )

    assistant_reply = response["message"]["content"].strip()
    history.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply


def cli_loop() -> None:
    print(f"🤖  Ollama chatbot ({MODEL_NAME}) ready — type 'exit' to quit\n")
    conversation: list[dict] = []

    try:
        while True:
            user = input("You: ").strip()
            if user.lower() in {"exit", "quit"}:
                break
            reply = get_reply(user, conversation)
            print("Bot:", reply)
    except KeyboardInterrupt:
        print("\n👋 Exiting...")


if __name__ == "__main__":
    cli_loop()
