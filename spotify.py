# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(taylor_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

import json
import unittest
import os
import requests

API_KEY = "b3476765b11a4d5488ca3b50a60bc761"

# http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
# https://api.spotify.com/v1/artists/b3476765b11a4d5488ca3b50a60bc761/albums?

def read_json(cache_filename):
    loaded_data = {}
    try:
        with open(cache_filename, 'r') as f:
            loaded_data = json.load(f)
            return loaded_data

    except:
        return loaded_data

def write_json(cache_filename, dict):
    with open(cache_filename, 'w') as json_file:
        json.dump(dict, json_file)
    pass



def get_data_using_cache(list, cache_filename):
    # Change this: (depends on list)
    request_url = 'http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6'
    loaded_data = read_json(cache_filename)

    if len(loaded_data) != 0:
        print(f"Using cache for {list}")
        return loaded_data
        #and makes a call to Books API to get the data the search

    else:
        print(f"Fetching data for {list}")
        response = requests.get(request_url)
        if response.ok:
            print("happened")
            write_json(cache_filename, loaded_data)
        
    if len(loaded_data) == 0:
        
        return None
    else:
        
        return loaded_data

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cache_filename = dir_path + '/' + "cache_bestseller.json"

    loaded_data = get_data_using_cache(list, cache_filename)
    print(loaded_data)



