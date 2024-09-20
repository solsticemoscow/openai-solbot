from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message
from pydantic import BaseModel


class MyCallbackCaptcha(CallbackData, prefix="captcha"):
    digit: int
    answer: int
    group: str

class DB(BaseModel):
    db_port: int
    db_name: str
    db_address: str
    db_pass: str
    db_user: str
    db_type: str

async def get_group_id(message: Message):
    print(message)


