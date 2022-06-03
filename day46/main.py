import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
import os

# setup pprint for easier understanding of results from spotipy searches
pp = pprint.PrettyPrinter(indent=4, compact=True)

# environment variables for spotify authentication
auth_manager = spotipy.SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                    client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                    redirect_uri=os.environ['SPOTIFY_REDIRECT_URI'],
                                    scope='playlist-modify-private')

# grab the auth token (or cached token) and set the user id
# auth_manager.get_access_token()
auth_manager.get_cached_token()
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()['id']

# grab input for the historical date wanting to parse
date = input("What year do you want to travel to? Enter in format YYYY-MM-DD")
year = date[:4]

# pull the URL off the billboard top 100
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
webpage = response.text

# grab the top 100 songs
soup = BeautifulSoup(webpage, "html.parser")
top_song = soup.find(name='h3', id='title-of-a-story', class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet')
song_list = soup.findAll(name='h3', id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

# alternative solution from another user...
# track_titles = soup.select("li ul li h3")

# turn the top 100 songs into a list
top100_list = []
top_song = top_song.getText().replace('\n', '').replace('\t', '')
top100_list.append(top_song)
for song in song_list:
    song_title = song.getText().replace('\n', '').replace('\t', '')
    top100_list.append(song_title)

# grab the uri for the top 100 songs (doesn't filter covers)
top100_uris = []
for song in top100_list:
    try:
        spotify_search = sp.search(f"track:{song} year:{year}", limit=1)['tracks']['items'][0]
        top100_uris.append(spotify_search['uri'])
    except:
        pass

# create the playlist and add the top 100 songs
playlist_name = f'{date} Billboard 100'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description='testing for coding project')
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=top100_uris)
