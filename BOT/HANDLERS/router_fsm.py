from aiogram.fsm.state import StatesGroup, State

import os

from aiogram import Bot, Router, F, flags
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, URLInputFile, FSInputFile
)

from aiogram.utils.markdown import link, hbold, hblockquote, hitalic, hcode
from BOT.UTILS.m_openai import ClassOpenAI
from BOT.config import ROOT_DIR, MSG_SOLBOT, PHOTO

router = Router()


class FSMSTATES(StatesGroup):
    IMAGEGENERATE = State()


@router.message(FSMSTATES.IMAGEGENERATE)
async def do_image(message: Message, bot: Bot, state: FSMContext):
    FROM: int = message.from_user.id
    TEXT = message.text


    await bot.send_message(
        chat_id=FROM,
        text='🖌️ ' + hbold(message.from_user.username) + ':\n\n' + hcode(TEXT))

    await bot.send_message(chat_id=FROM, text=hbold(MSG_SOLBOT) + hitalic("Генерирую изображение..."))

    result = await ClassOpenAI.get_image(PROMT=TEXT)

    await bot.send_photo(
        chat_id=FROM,
        caption=hbold(MSG_SOLBOT) + hitalic('Готово!'),
        photo=URLInputFile(result)
    )
    await state.clear()
