#%%
import os

import lyricsgenius
from dotenv import load_dotenv

load_dotenv()

#%%
os.getenv('GENIUS_API_TOKEN')

#%%
genius = lyricsgenius.Genius(os.getenv('GENIUS_API_TOKEN'))
#%%
artist = genius.search_artist("Perfume", max_songs=3, sort="title")
print(artist.songs)
#%%
song = artist.song("1mm")
print(song.lyrics)
#%%
