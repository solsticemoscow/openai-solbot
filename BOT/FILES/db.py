import asyncio
import hashlib

from sqlalchemy import insert, select, create_engine, BigInteger, Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped

from app.models.tables import DBModel

engine = create_engine(
    url='sqlite:///db.db', echo=False, pool_pre_ping=True
)

db_session = sessionmaker(engine, autoflush=False, expire_on_commit=False)

class Users(DBModel):
    __tablename__ = 'Users'


    telegram: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    counter: Mapped[int] = mapped_column(Integer)

    @hybrid_property
    def counter(self):
        return self.hours * self.payrate.hourly

    @counter.expression
    def counter(cls):
        return cls.hours * payrate_derived.c.hourly



with db_session() as session:
    stmt = select(UsersProject2).where(UsersProject2.login == '2')
    result = session.execute(statement=stmt)
    user = result.one_or_none()
    if user:
        data = user[0]
    print(data.tags)
