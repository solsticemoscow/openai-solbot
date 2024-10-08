import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommandScope, BotCommand, ReplyKeyboardRemove, \
    BotCommandScopeAllChatAdministrators, URLInputFile, BotCommandScopeAllGroupChats, WebAppInfo, MenuButtonWebApp
from aiogram.utils.markdown import hitalic, hblockquote, hpre, html_decoration, hbold

from BOT.HANDLERS.router_first import ROUTER

from aiogram import Bot, Dispatcher

from BOT.UTILS.middlewares import ThrottlingMiddleware
from BOT.config import SOLBOT_TOKEN, TG_SOLSTICE, MSG_SOLBOT, WEBAPPURL

storage = MemoryStorage()

BOT = Bot(token=SOLBOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
DP = Dispatcher()


DP.include_router(ROUTER)
DP.message.middleware.register(ThrottlingMiddleware())




async def solbot():

    print('Bot start!')




    await BOT.send_message(
        chat_id=TG_SOLSTICE,
        text=hbold(MSG_SOLBOT) + hitalic('Искусственный Интеллект готов двигать прогресс! PS. Картинки голых людей не генерирую)'),
        reply_markup=ReplyKeyboardRemove()
    )


    await DP.start_polling(BOT)

if __name__ == "__main__":
    asyncio.run(solbot())

