import os

from aiogram import Bot, Router, F, flags

from aiogram.utils.markdown import link, code, blockquote, hcode, bold, italic, hlink, hbold, hitalic, hblockquote
from aiogram.fsm.context import FSMContext

from aiogram.types import (
    Message, CallbackQuery, FSInputFile,
    URLInputFile, MessageReactionUpdated, ErrorEvent, InputMediaPhoto
)


from BOT.UTILS.m_openai import ClassOpenAI
from BOT.UTILS.m_utils import UtilsClass

from BOT.config import TG_SOLSTICE, MSG_SOLBOT, PHOTO, TEST_GROUP

router = Router()

# @router.message(F.text.lower().contains('/1'), F.chat.type == 'group', F.chat.type == 'supergroup')
# async def tag_ld_players(message: Message):
#
#     print(message.text)
#







@router.message(F.text, F.chat.type == 'private')
async def get_text(message: Message, bot: Bot, state: FSMContext):

    TEXT = message.text


    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text='🖌️ ' + hbold(message.from_user.username) + ':\n\n' + hcode(TEXT))


    data = await state.get_data()

    if data:
        if data['vision']:
            response = await ClassOpenAI.get_vision(image_path=data['image_url'])

            await bot.send_message(
                chat_id=message.from_user.id,
                text=hbold(MSG_SOLBOT) + hcode(response),
            )

    else:
        await ClassOpenAI.add_dialog(content=TEXT, role='user')

        response = await ClassOpenAI.get_text(MSGS=ClassOpenAI.MSGS)

        await ClassOpenAI.add_dialog(content=response, role='assistant')

        await bot.send_message(
            chat_id=message.from_user.id,
            text=hbold(MSG_SOLBOT) + hcode(response),
        )



@router.callback_query()
async def get_callback(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.answer()

    CALLBACK = call.data
    print(f'CALLBACK: {CALLBACK}')

    data = await state.get_data()

    if CALLBACK == 'yt_mp3':
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=hbold(MSG_SOLBOT) + hitalic('Секунду, начинаю качать аудио с Youtube...'),
        )
        res = UtilsClass.get_content_from_youtube(URL=data['url'], TYPE=CALLBACK)

        await bot.send_audio(
            duration=res[0],
            chat_id=call.message.chat.id,
            audio=FSInputFile(path=res[1])
        )
        os.remove(res[1])
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=hbold(MSG_SOLBOT) + hitalic('Готово!'),
        )
    if CALLBACK == 'yt_mp4':
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=hbold(MSG_SOLBOT) + hitalic('Секунду, начинаю качать видео с Youtube...'),
        )
        res = UtilsClass.get_content_from_youtube(URL=data['url'], TYPE=CALLBACK)

        await bot.send_video(
            duration=res[0],
            width=1920,
            height=780,
            chat_id=call.message.chat.id,
            video=FSInputFile(path=res[1])
        )
        os.remove(res[1])
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=hbold(MSG_SOLBOT) + hitalic('Готово!'),
        )


@router.message()
async def get_all(message: Message, bot: Bot):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(chat_id=message.from_user.id, text=hbold(MSG_SOLBOT) + hitalic("Такое я не поддерживаю."))


@router.errors()
async def error_handler(exception: ErrorEvent, bot: Bot):
    print(f'ERROR: {exception.exception}')
    await bot.send_message(
        chat_id=TG_SOLSTICE,
        text=f'֎ *У меня сбой*:\n\n{str(exception.exception)}.',
    )
