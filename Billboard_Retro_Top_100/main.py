from date_format import DateConverter
from billboard_data import BillboardData
from spotify import Spotify

date_input = input("Which date do you want to travel to?: ")
date = ""
try:
    date = DateConverter().convert_date(date_input)
except TypeError:
    print("wrong Data")

print(date)

billboard_data = BillboardData(date)

songs = billboard_data.get_songs()
artists = billboard_data.get_artists()
songs_uri = []
spotify = Spotify()

for index in range(0, len(songs)):
    song = songs[index]
    artist = artists[index]
    song_uri = spotify.search_song(song, artist)
    songs_uri.append(song_uri)


playlist = spotify.create_playlist(date)


spotify.add_to_playlist(playlist, songs, songs_uri)

