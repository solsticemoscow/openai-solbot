import asyncio
from typing import NoReturn

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommandScope, BotCommand, ReplyKeyboardRemove, \
    BotCommandScopeAllChatAdministrators, URLInputFile
from aiogram.utils.markdown import hitalic, hblockquote, hpre, html_decoration, hbold

from BOT.UTILS.middlewares import UserFilterMiddleware
from BOT.config import SOLBOT_TOKEN, TG_SOLSTICE, MSG_SOLBOT

from aiogram import Bot, Dispatcher

from BOT.HANDLERS.router_first import ROUTER


BOT = Bot(token=SOLBOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
DP = Dispatcher()
DP.message.middleware(middleware=UserFilterMiddleware())
DP.include_router(ROUTER)


