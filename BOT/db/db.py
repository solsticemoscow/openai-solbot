import asyncio

from sqlalchemy import insert, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from BOT.config import DB_MYSQL
from BOT.db.tables import Users

ENGINE = create_async_engine(
    DB_MYSQL,
    echo=False,
    pool_pre_ping=True
)

async_session = async_sessionmaker(ENGINE, autoflush=True, expire_on_commit=False)
DB_SESSION = async_session()


async def db_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# async  def f1():
#     async with DB_SESSION:
#         stmt = insert(Users).values(
#             id=5675678,
#             username="message.from_user.username",
#             firstname="message.from_user.first_name",
#             lastname="message.from_user.last_name",
#             language_code="message.from_user.language_code",
#             time_added=func.now()
#         )
#         await DB_SESSION.execute(statement=stmt)
#         await DB_SESSION.commit()
#
#
#
# asyncio.run((f1()))
