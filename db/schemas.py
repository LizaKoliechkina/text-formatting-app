from sqlalchemy import Boolean, Enum, Column, String, Integer, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
# from db.db_session import Base
from server.format import Filter

Base = declarative_base()


class FormatText(Base):
    __tablename__ = 'format_text'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    done = Column(Boolean, default=False)


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    text_id = Column(Integer, ForeignKey('format_text.id'), nullable=False)
    formatted = Column(String, nullable=False)
    filter = Column(Enum(Filter), nullable=False)
    queue = Column(Integer, nullable=False)
