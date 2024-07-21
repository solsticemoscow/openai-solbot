

from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message
)

from aiogram.utils.markdown import hbold, hitalic

from BOT.HANDLERS.router_content import router as router_content
from BOT.HANDLERS.router_fsm import FSMSTATES
from BOT.HANDLERS.router_last import router as router_last
from BOT.HANDLERS.router_fsm import router as router_fsm





from BOT.config import MSG_SOLBOT, TEST_GROUP

ROUTER = Router()


ROUTER.include_router(router=router_content)
ROUTER.include_router(router=router_fsm)
ROUTER.include_router(router=router_last)


@ROUTER.message(Command(commands=["start"]), F.chat.type == 'private')
async def command_start(message: Message, bot: Bot, state: FSMContext):
    FROM: int = message.from_user.id
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(
        chat_id=FROM,
        text=hbold(MSG_SOLBOT) + hitalic('Я перезагрузился и готов помогать!'),
    )

    await state.clear()

@ROUTER.message(Command(commands=["image"]), F.chat.type == 'private')
async def command_generate_image(message: Message, bot: Bot, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text=hbold(MSG_SOLBOT) + hitalic('Какое изображение вам нужно?'))

    await state.set_state(FSMSTATES.IMAGEGENERATE)






