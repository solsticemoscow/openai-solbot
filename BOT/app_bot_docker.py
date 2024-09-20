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

    await BOT.set_chat_menu_button(
        chat_id=TG_SOLSTICE,
        menu_button=MenuButtonWebApp(text="🔎 ПОИСК", web_app=WebAppInfo(url=f"{WEBAPPURL}/"))
    )

    await BOT.set_my_commands([
        BotCommand(command='start', description='Start menu'),
        BotCommand(command='get_image', description='Сгенерировать картинку'),
    ],
        scope=BotCommandScopeDefault()
    )


    await BOT.send_message(
        chat_id=TG_SOLSTICE,
        text=hbold(MSG_SOLBOT) + hitalic('Искусственный Интеллект готов двигать прогресс! PS. Картинки голых людей не генерирую)'),
        reply_markup=ReplyKeyboardRemove()
    )


    await DP.start_polling(BOT)

if __name__ == "__main__":
    asyncio.run(solbot())

