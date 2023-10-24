from sqlalchemy import Column, Integer, String, ARRAY, DateTime, TIMESTAMP, func, VARCHAR, JSON
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://alphabet:12345678@127.0.0.1/alphabet', echo=True)

Base = declarative_base()


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(32))
    participants = Column(JSON)
    location = Column(VARCHAR(32))
    date = Column(DateTime)
    creation_time = Column(TIMESTAMP, server_default=func.now())


table = [Events.__table__]
Base.metadata.create_all(engine, tables=table)
