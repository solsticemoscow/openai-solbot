from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold, hitalic
from cache3 import Cache
from aiogram import BaseMiddleware, Bot
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from BOT.config import ADMINS, MSG_SOLBOT, SOLBOT_TOKEN


class UserFilterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id in ADMINS:
            return await handler(event, data)
        else:
            await event.delete()


# cache = Cache(name='counters')
#
# class RateLimitMiddleware(BaseMiddleware):
#
#
#     async def __call__(
#         self,
#         handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#         event: Message,
#         data: Dict[str, Any]
#     ) -> Any:
#         print(data)
#         print(event)
#         if event.from_user.id not in ADMINS:
#             cache.set(key=event.from_user.id, value=True, timeout=15)
#             if cache[event.from_user.id]:
#                 return event.answer(text='Подождите 15 секунд, чтобы снова обратиться к боту.')
#             else:
#                 await event.answer(event.text)
#                 return await handler(event, data)











