from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Song(Base):
	__tablename__ = 'songs'
	id = Column(Integer, primary_key=True)
	song_name = Column(String)
	mood = Column(String)
	description = Column(String)
	song_link = Column(String)