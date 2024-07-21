import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Embeddings(Base):
    __tablename__ = 'embeddings'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Embedding = Column(JSON, nullable=False)


sqliteConnection = sqlite3.connect('../FILES/db.db')