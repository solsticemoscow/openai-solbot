import os
import random


from aiogram import Bot, Router, F, flags
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.utils.markdown import link, code, blockquote, hcode, bold, italic, hlink, hbold, hitalic, hblockquote
from aiogram.fsm.context import FSMContext

from aiogram.types import (
    Message, CallbackQuery, FSInputFile,
    URLInputFile, MessageReactionUpdated, ErrorEvent, InputMediaPhoto, InlineKeyboardButton, ChatPermissions
)

from sqlalchemy import select, func, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from BOT.UTILS.custom import MyCallbackCaptcha
from BOT.UTILS.m_openai import ClassOpenAI
from BOT.UTILS.m_utils import UtilsClass


from BOT.config import TG_SOLSTICE, MSG_SOLBOT, PHOTO, TEST_GROUP, ADMINS
from BOT.db.db import DB_SESSION, async_session
from BOT.db.tables import Users, Admin

router = Router()


@router.callback_query(MyCallbackCaptcha.filter())
async def callback_query_handler(call: CallbackQuery, bot: Bot, callback_data: MyCallbackCaptcha,
                                 db: AsyncSession = async_session()):
    await call.answer()


    FROM: int = call.from_user.id
    USER_NAME: str = call.from_user.username
    CALLBACK: str = call.data

    print(f'CALL ALL: {CALLBACK}')

    if callback_data:
        DIGIT = callback_data.digit


        stmt = select(Users.captcha).where(Users.id == FROM)
        result = await db.execute(stmt)
        captcha = result.scalar()

        if DIGIT == captcha:
            stmt = update(Users).values(
                captcha=True
            ).where(Users.id == FROM)
            await db.execute(stmt)
            await db.commit()

            await bot.restrict_chat_member(
                chat_id=callback_data.message.chat.id,
                user_id=FROM,
                permissions=ChatPermissions(
                    can_send_messages=True,
                    can_send_audios=True,
                    can_send_polls=True,
                    can_send_photos=True,
                    can_send_videos=True,
                    can_send_documents=True,
                )
            )

            TEXT = (f'✨ <b>Это бот нового поколения для администрирования телеграмм-групп!</b>\n\n'
                    f'<i>✅ Вы успешно прошли проверку и теперь можете писать в группе</i> <b>{callback_data.group}</b>!')

            await bot.send_message(
                chat_id=FROM,
                text=TEXT
            )
        else:
            TEXT = (f'✨ Пройдите проверку, чтобы писать в этой группе. Выберите наименьшее число:\n\n' + hlink(
                title='GROUP', url='t.me/dfghrth567'))

            random_integer1 = random.randint(0, 100)
            random_integer2 = random.randint(0, 100)
            random_integer3 = random.randint(0, 100)

            async with DB_SESSION:
                stmt = update(Users).where(Users.id == FROM).values(
                    captcha_value=min(random_integer1, random_integer2, random_integer3))
                await DB_SESSION.execute(statement=stmt)
                await DB_SESSION.commit()

            KB = InlineKeyboardBuilder()
            KB.add(InlineKeyboardButton(
                text=f'{random_integer1}',
                callback_data=MyCallbackCaptcha(digit=random_integer1,
                                                group=call.message.chat.title,
                                                answer=min(random_integer1, random_integer2,
                                                           random_integer3)).pack()
            ))
            KB.add(InlineKeyboardButton(
                text=f'{random_integer2}',
                callback_data=MyCallbackCaptcha(digit=random_integer2,
                                                group=call.message.chat.title,
                                                answer=min(random_integer1, random_integer2,
                                                           random_integer3)).pack()
            ))
            KB.add(InlineKeyboardButton(
                text=f'{random_integer3}',
                callback_data=MyCallbackCaptcha(digit=random_integer3,
                                                group=call.message.chat.title,
                                                answer=min(random_integer1, random_integer2,
                                                           random_integer3)).pack()
            ))
            KB.adjust(3)

            await bot.send_message(
                chat_id=FROM,
                text=TEXT,
                reply_markup=KB.as_markup()
            )





@router.message(F.text, F.chat.type == 'private')
async def get_text(message: Message, bot: Bot, state: FSMContext):
    USER_ID: int = message.from_user.id
    TEXT = message.text

    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await bot.send_chat_action(chat_id=USER_ID, action='typing')
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

# @router.message()
# async def get_all(message: Message, bot: Bot):
#     print(f' From all: {message}')
#
#     await bot.send_message(chat_id=message.from_user.id, text=hbold(MSG_SOLBOT) + hitalic("Такое я не поддерживаю."))


# @router.errors()
# async def error_handler(exception: ErrorEvent, bot: Bot):
#     print(f'ERROR: {exception.exception}')
#     await bot.send_message(
#         chat_id=TG_SOLSTICE,
#         text=f'֎ *У меня сбой*:\n\n{str(exception.exception)}.',
#     )
