


from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, TelegramObject
from typing import Callable, Dict, Any, Awaitable

from sqlalchemy import select

from BOT.config import ADMINS, MSG_SOLBOT, SOLBOT_TOKEN
from BOT.db.db import async_session
from BOT.db.tables import Users




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


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_process_message(self, message, data, *args):
        async with async_session() as session:
            stmt = select(Users)
            result = await session.execute(statement=stmt)
            all = result.scalars()
            print(all)

        return all

from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from cachetools import TTLCache


def throttled(rate: int, on_throttle: Callable or None = None):
    """Throttled decorator, must be above router/dispatcher decorator!!!

    Args:
        rate (int): Determines how long the user will have to wait (seconds) to use again.
        on_throttle (Callable or None, optional): Callback function if rate limit exceed. Defaults to None.
    """

    def decorator(func):
        setattr(func, "rate", rate)
        setattr(func, "on_throttle", on_throttle)
        return func

    return decorator


class ThrottlingMiddleware(BaseMiddleware):
    """
    Throttling middleware which is used as an anti-spam tool
    1. Initialize and attach to router/dispatcher
    2. Use @throttled(rate, on_throttle) above router decorator
    """

    def __init__(self, rate=None):
        # self.cache = TTLCache(maxsize=10_000, ttl=self.delay)
        self.caches = dict()
        self.rate = rate

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:

        decorated_func = data["handler"].callback
        rate = getattr(decorated_func, "rate", None)
        if rate is None and self.rate is None:
            rate = 1
        elif rate is None:
            rate = self.rate
        on_throttle = getattr(decorated_func, "on_throttle", None)

        if rate and isinstance(rate, int) and rate > 0:  # Check if rate arg passed and passed correctly (decorator check)
            if id(decorated_func) not in self.caches:  # Check if func TTL already in dict. If not - create it.
                self.caches[id(decorated_func)] = TTLCache(maxsize=10_000, ttl=rate)

            if event.chat.id in self.caches[id(decorated_func)].keys():
                if callable(on_throttle):
                    return await on_throttle(event, data)
                else:
                    return
            else:
                self.caches[id(decorated_func)][event.chat.id] = event.chat.id
                return await handler(event, data)
        else:
            return await handler(event, data)
