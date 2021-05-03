#%%
import os

import lyricsgenius
from dotenv import load_dotenv

load_dotenv()

genius = lyricsgenius.Genius(os.getenv('GENIUS_API_TOKEN'))

#%%
artists = ['Perfume']
for aName in artists:
    print(aName)
    artist = genius.search_artist(aName)
    artist.save_lyrics()

#%%
import json

#%%
with open('./Lyrics_Perfume.json') as f:
    data = json.load(f)
    
#%%
for song in data['songs']:
    print(song['title'])
    print(song['lyrics'])
