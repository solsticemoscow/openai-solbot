import datetime
import json
import uuid

from typing import Annotated, Optional

import sqlalchemy
from sqlalchemy import Boolean, String, BigInteger, Integer, ForeignKey, Enum, DateTime, Column, Text, select, func, \
    SQLColumnExpression, JSON, ARRAY, insert, TIME

from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base, column_property, ColumnProperty


MAP_BOOL = Annotated[Optional[bool], mapped_column(default=False, nullable=True)]
MAP_STR = Annotated[Optional[str], mapped_column(String(255), nullable=True)]
MAP_INT = Annotated[Optional[int], mapped_column(nullable=True)]
MAP_BIGINT = Annotated[Optional[int], mapped_column(BigInteger, nullable=True)]
MAP_TEXT = Annotated[Optional[Text], mapped_column(sqlalchemy.Text, nullable=True)]


DBModel = declarative_base()

class Users(DBModel):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(200), nullable=True)
    firstname: Mapped[str] = mapped_column(String(200), nullable=True)
    lastname: Mapped[str] = mapped_column(String(200), nullable=True)
    language_code: Mapped[str] = mapped_column(String(20), nullable=True)
    profile_description: Mapped[str] = mapped_column(Text, nullable=True)

    time_added: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    blocked: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)
    captcha: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)
    captcha_value: Mapped[int] = mapped_column(Integer, primary_key=True)


class Admin(DBModel):
    __tablename__ = 'Admin'

    id: Mapped[str] = mapped_column(String(100), primary_key=True, default=uuid.uuid4())
    captcha: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)



# class Channels(DBModel):
#     __tablename__ = 'Channels'
#
#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
#     channel_name: Mapped[str] = mapped_column(String(100), nullable=True)
#
#     user_id: Mapped[int] = mapped_column(ForeignKey('Users.id'), nullable=True)
#     channels_to_user = relationship('Users', back_populates='user_to_channels')






