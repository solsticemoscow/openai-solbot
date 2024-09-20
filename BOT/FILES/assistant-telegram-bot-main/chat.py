from admin import get_assistant_id
from config import get_config, proxy_client, save_config


def get_thread_id(chat_id: str):
    config = get_config()
    if "threads" not in config:
        config["threads"] = {}

    if chat_id not in config["threads"]:
        thread = proxy_client.beta.threads.create()
        config["threads"][chat_id] = thread.id
        save_config(config)

    return config["threads"][chat_id]


def process_message(chat_id: str, message: str) -> list[str]:
    assistant_id = get_assistant_id()
    thread_id = get_thread_id(chat_id)
    proxy_client.beta.threads.messages.create(
        thread_id=thread_id, content=message, role="user"
    )

    run = proxy_client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    answer = []

    if run.status == "completed":
        messages = proxy_client.beta.threads.messages.list(
            thread_id=thread_id, run_id=run.id
        )
        for message in messages:
            if message.role == "assistant":
                for block in message.content:
                    if block.type == "text":
                        answer.append(block.text.value)

    return answer
