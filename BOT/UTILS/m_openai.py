import asyncio
import base64
import os

import requests

from openai import AsyncOpenAI

from BOT.UTILS.m_utils import UtilsClass
from BOT.config import MODEL_VOICE, PROMT2, OPENAI_API, VECTOR

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_internet_search",
            "description": "Get the info from Internet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "User query."
                    },
                },
                "required": ["query"]
            }
        }
    }
]


class ClassOAI:

    def __init__(self):
        self.vision = False
        self.tools = tools
        self.MSGS = []
        self.llm = AsyncOpenAI(
            max_retries=3,
            timeout=15,
            api_key=OPENAI_API
        )

    async def get_vector(self):
        assistant = await self.llm.beta.assistants.create(
            instructions="Ты помогаешь в .",
            model="gpt-4o",
            tools=[{"type": "file_search"}],
            tool_resources={
                "file_search": {
                    "vector_store_ids": [VECTOR]
                }
            }
        )

        thread = await self.llm.beta.threads.create()

        thread_message = await self.llm.beta.threads.messages.create(
            thread.id,
            role="user",
            content="Найди все мои телефоны",
        )

        run = await self.llm.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        message = await self.llm.beta.threads.messages.retrieve(
            message_id=thread_message.id,
            thread_id=thread.id,
        )
        print(message.content[0].text)

    async def get_vision(
            self,
            image_path: str
    ):

        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

        base64_image = encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API}"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": PROMT2
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 200
        }

        try:
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return e

    async def add_dialog(self, content: str, role: str):
        message = {
            "role": role,
            "content": content
        }
        self.MSGS.append(message)
        return self.MSGS

    async def reset_dialog(self):
        self.MSGS.clear()

    async def get_image(self, PROMT: str):
        try:
            image = await self.llm.images.generate(
                model="dall-e-3",
                response_format='url',
                n=1,
                quality='hd',
                prompt=PROMT
            )
            if image.data[0].url:
                return image.data[0].url
        except Exception as e:
            return e

    async def get_embedding(self, promt: str = 'Адрес: Одинцово, Немчиновка, Рублевский проезд, д. 20А, кв. 107.'):
        try:
            response = await self.llm.embeddings.create(
                input=promt,
                model="text-embedding-3-small"
            )
            return response.data[0].embedding
        except Exception as e:
            return e

    async def get_text(self, MSGS: list):
        try:
            response = await self.llm.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=MSGS,
                max_tokens=700,
                temperature=0.7
            )
            answer = response.choices[0].message
            return answer.content

        except Exception as e:
            return e

    async def get_voice(self, VOICE: str):
        try:
            with open(VOICE, "rb") as audio_file:
                transcript = await self.llm.audio.transcriptions.create(
                    model=MODEL_VOICE,
                    file=audio_file
                )
                return str(transcript.text)
        except Exception as e:
            return e


ClassOpenAI = ClassOAI()

# async def f1():
#     MSGS = await ClassOpenAI.add_dialog(content='radeon rx 570 год выпуска', role='user')
#     print(MSGS)
#
#     return await ClassOpenAI.get_text(MSGS=MSGS)
#
# print(asyncio.run(f1()))