import json
import os

from aiogram import Bot, Router, F, flags
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, URLInputFile, FSInputFile
)

from aiogram.utils.markdown import link, hbold, hblockquote, hitalic, hcode

from BOT.UTILS.keys import MK
from BOT.UTILS.m_openai import ClassOpenAI

from BOT.config import ROOT_DIR, MSG_SOLBOT, PHOTO

router = Router()



@router.message(F.web_app_data)
async def web_app_data_handler(message: Message):
    data = message.web_app_data.data
    time_data = json.loads(data)
    hours = time_data.get('hours')
    minutes = time_data.get('minutes')

    # Send confirmation message to the user
    await message.answer(f'Selected time: {hours}:{minutes}')


@router.message(F.voice, F.chat.type == 'private')
async def do_voice(message: Message, bot: Bot):
    USER_ID: int = message.from_user.id
    VOICE_ID: str = message.voice.file_id
    FILEPATH = ROOT_DIR + f'/FILES/{message.voice.file_id}.ogg'


    await bot.send_chat_action(chat_id=USER_ID, action='typing')
    await bot.download(file=VOICE_ID, destination=FILEPATH)

    ASNWER = await ClassOpenAI.get_voice(FILEPATH)

    MSGS = await ClassOpenAI.add_dialog(content=ASNWER, role='user')

    await bot.send_message(
        chat_id=USER_ID,
        text='🖌️ ' + hbold(message.from_user.username) + ':\n\n' + hcode(ASNWER))

    response = await ClassOpenAI.get_text(MSGS=MSGS)

    await ClassOpenAI.add_dialog(content=response, role='assistant')

    await bot.send_message(
        chat_id=USER_ID,
        text=hbold(MSG_SOLBOT) + hcode(response),
    )

    os.remove(FILEPATH)


@router.message(F.photo, F.chat.type == 'private')
async def do_voice(message: Message, bot: Bot, state: FSMContext):


    FROM: int = message.from_user.id
    PHOTO_ID: str = message.photo[-1].file_id
    FILENAME: str = message.photo[-1].file_unique_id + '.jpg'
    FILEPATH = ROOT_DIR + f'/FILES/{FILENAME}'

    await bot.send_message(chat_id=FROM, text=hbold(MSG_SOLBOT) + hitalic("Секунду, получил изображение..."))
    await bot.get_file(file_id=PHOTO_ID)
    await bot.download(file=PHOTO_ID, destination=FILEPATH)


    result = await ClassOpenAI.get_vision(image_path=FILEPATH)

    await bot.send_message(chat_id=FROM, text=hbold(MSG_SOLBOT) + hcode(result))

    await ClassOpenAI.add_dialog(content=result, role='assistant')

    os.remove(FILEPATH)


@router.message(F.audio)
async def do_audio(message: Message, bot: Bot, state: FSMContext):


    FROM: int = message.from_user.id
    PHOTO_ID: str = message.audio.file_id
    FILENAME: str = message.photo[-1].file_unique_id + '.jpg'
    FILEPATH = ROOT_DIR + f'/FILES/{FILENAME}'

    await bot.get_file(file_id=PHOTO_ID)
    await bot.download(file=PHOTO_ID, destination=FILEPATH)


    result = await ClassOpenAI.get_vision(image_path=FILEPATH)

    await bot.send_message(chat_id=FROM, text=hbold(MSG_SOLBOT) + hcode(result))

    await ClassOpenAI.add_dialog(content=result, role='assistant')

    await state.set_data(data={
        'vision': True,
        'image_url': FILEPATH
    })

    os.remove(FILEPATH)


# @router.message(F.chat.type == 'private', F.text.contains("www.shazam"))
# async def get_text(message: Message, bot: Bot, state: FSMContext):
#     USER_ID: int = message.from_user.id
#     TEXT = message.text
#     QUERY = message.text.split(sep='https:')[0]
#
#     url = UtilsClass.get_info_from_youtube(QUERY=QUERY)
#
#     await bot.delete_message(chat_id=USER_ID, message_id=message.message_id)
#     await bot.send_message(
#         chat_id=USER_ID,
#         text=hbold(MSG_SOLBOT) + hitalic(f'получил ссылку Шазам...\n\n{TEXT}'),
#         reply_markup=MK.in_yt()
#
#     )
#
#     await state.set_data(data={'url': url})
#
#
#
@router.message(F.chat.type == 'private', F.text.regexp(
    r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'))
async def get_youtube(message: Message, bot: Bot, state: FSMContext):
    USER_ID: int = message.from_user.id
    url = message.text

    await bot.delete_message(chat_id=USER_ID, message_id=message.message_id)

    await bot.send_message(
        chat_id=USER_ID,
        text=hbold(MSG_SOLBOT) + hitalic(f'Получил ссылку Youtube...\n\n{url}'),
        reply_markup=MK.in_yt(),
    )

    await state.set_data(data={'url': url})







