from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def creat_song(song_name, mood, description, song_link):
	song = Song(song_name = song_name, mood = mood, description=description, song_link = song_link)
	session.add(song)
	session.commit()


def get_song_by_song_name(song_name):
	song = session.query(Song).filter_by(song_name = song_name).first()
	return song


def edit_song(song_name, mood, description, song_link):
	song = get_song_by_song_name(song_name)
	song.mood = mood
	song.description = description
	song.song_link = song_link


def get_songs_by_mood(mood):
	songs = session.query(Song).filter_by(mood = mood)
	return list(songs)

def delete_song(song_name):
	session.query(User).filter_by(song_name = song_name).delete()
	session.commit()


creat_song("song1", "happy", "coool", "dksvhkal")
creat_song("song2", "happy", "coool123", "vdsvdsvdsvds")
creat_song("song2", "sad", "not_cool", "vrqleiajfkv")

print(get_songs_by_mood("happy"))