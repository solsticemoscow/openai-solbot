from aiogram import Bot, Router, F, flags
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
)

from aiogram.utils.markdown import hbold, hitalic


from sqlalchemy import func, insert

from BOT.HANDLERS.router_content import router as router_content
from BOT.HANDLERS.router_fsm import FSMSTATES
from BOT.HANDLERS.router_last import router as router_last
from BOT.HANDLERS.router_fsm import router as router_fsm
from BOT.UTILS.middlewares import throttled

from BOT.config import MSG_SOLBOT, TEST_GROUP, WEBAPPURL
from BOT.db.db import DB_SESSION
from BOT.db.tables import Users

ROUTER = Router()

ROUTER.include_router(router=router_content)
ROUTER.include_router(router=router_fsm)
ROUTER.include_router(router=router_last)


@throttled(rate=5)
@ROUTER.message(Command(commands=["start"]), F.chat.type == 'private')
async def command_start(message: Message, bot: Bot, state: FSMContext):
    FROM: int = message.from_user.id

    await bot.send_message(
        chat_id=FROM,
        text=hbold(MSG_SOLBOT) + hitalic('Я перезагрузился и готов помогать!'),
    )
    try:
        async with DB_SESSION:
            stmt = insert(Users).values(
                id=message.from_user.id,
                username=message.from_user.username,
                firstname=message.from_user.first_name,
                lastname=message.from_user.last_name,
                language_code=message.from_user.language_code,
                time_added=func.now()
            )
            await DB_SESSION.execute(statement=stmt)
            await DB_SESSION.commit()

    except Exception as e:
        print(e)
        await bot.delete_message(message.from_user.id, message.message_id)
        await state.clear()


@throttled(rate=60)
@ROUTER.message(Command(commands=["image"]), F.chat.type == 'private')
async def command_generate_image(message: Message, bot: Bot, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text=hbold(MSG_SOLBOT) + hitalic('Какое изображение вам нужно?'))

    await state.set_state(FSMSTATES.IMAGEGENERATE)


@ROUTER.message(Command(commands=["reset"]), F.chat.type == 'supergroup')
async def command_generate_image(message: Message, bot: Bot, state: FSMContext):
    await bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_audios=True,
            can_send_polls=True,
            can_send_photos=True,
            can_send_videos=True,
            can_send_documents=True,
        )
    )


@ROUTER.message(Command(commands=["test"]))
async def command_generate_image(message: Message, bot: Bot, state: FSMContext):
    await message.answer(
        text="<i>🔧 Open your settings:</i>",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🛠 Settings", web_app=WebAppInfo(url=f"{WEBAPPURL}/settings"))]
            ]
        )
    )
