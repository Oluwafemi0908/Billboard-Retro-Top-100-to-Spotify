import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import unicodedata


class Spotify:
    def __init__(self):
        self.song_url = None
        self.track = None
        self.artist_name = None
        self.song_response = None
        self.song_uri = None
        self.client_id = "bcf713c5a2e1438691b064068eeb350d"
        self.client_secret = "f9f1fa540d20457db9a84d3f53b6305a"
        self.search_num = 0
        sp = SpotifyOAuth(client_id=self.client_id,
                          client_secret=self.client_secret,
                          redirect_uri="http://example.com/",
                          scope="playlist-modify-private playlist-read-private",
                          username="Oluwafemi Akinode",
                          show_dialog=True,
                          cache_path="token.txt",
                          )

        self.client = spotipy.Spotify(auth_manager=sp)
        self.song_name = ""
        self.user_id = self.client.current_user()['id']

    def search_song(self, query, artist):
        def check_artist(prt_str):
            print(prt_str)

        def remove_accents(text):
            return ''.join(c for c in unicodedata.normalize('NFD', text)
                           if unicodedata.category(c) != 'Mn')

        try:
            self.song_response = self.client.search(q=query, limit=20, type="track")
            for idx, track in enumerate(self.song_response["tracks"]["items"]):
                self.track = track
                self.song_name = track["name"]
                self.song_name = remove_accents(self.song_name)
                self.artist_name = track["artists"][0]["name"].strip()
                self.artist_name = remove_accents(self.artist_name)
                self.song_url = track["external_urls"]["spotify"]
                artists = re.split(r'[\sxX,;._&-]+', artist.lower())
                sp_artist = re.split(r'[\sxX,;._&-]+', self.artist_name.lower())
                # print(artists)
                # print(sp_artist)
                if self.artist_name.lower() == artist.lower():
                    print_string = f"{self.song_name} by {self.artist_name}: {self.song_url}"
                    self.song_uri = track["uri"]
                    check_artist(print_string)
                    return self.song_uri

                else:
                    for a_name in sp_artist:
                        for b_name in artists:
                            # print(a_name)
                            # print(b_name)
                            if a_name == b_name:
                                print_string = f"{self.song_name} by {self.artist_name}: {self.song_url}"
                                self.song_uri = track["uri"]
                                check_artist(print_string)
                                return self.song_uri
            self.song_uri = f"{query} by {artist} not found."
            print_string = self.song_uri
            self.search_num = len(self.song_response["tracks"]["items"])
            check_artist(print_string)
            return self.song_uri
        except:
            # return f"{query} by {artist} not found."
            pass

    def create_playlist(self, date):
        playlist_title = f"{date} Billboard 100"
        playlists = self.client.user_playlists(limit=50, user=self.user_id)  # Fetch up to 50 playlists
        for playlist in playlists["items"]:
            if playlist["name"].lower() == playlist_title.lower():
                print(f"✅ Playlist '{playlist_title}' exists! ID: {playlist['id']}")
                return playlist['id']
        print(f"Creating {playlist_title}")
        description = f"Want to travel back in time to top hit as at {date}? SPOTIFY got you covered"
        new_playlist = self.client.user_playlist_create(user=self.user_id, name=playlist_title,
                                                        description=description, public=False)
        print(f"{playlist_title} created successfully")
        return new_playlist["id"]

    def add_to_playlist(self, playlist, song_list, song_uri_list):
        for song in song_list:
            song_uri = song_uri_list[song_list.index(song)]
            print(song_uri)
            song_uri_x = [song_uri]
            print(song_uri_x)
            try:
                self.client.playlist_add_items(playlist_id=playlist, items=song_uri_x)
                print(f"{song} added successfully")
            except Exception as e:
                print(f"{e}: {song_uri}")
        print("\n\nPlaylist updated Successfully!!!")
