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
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


searchUrl = 'https://api.spotify.com/v1/search'
artistId_lst = []
API_KEY = "b3476765b11a4d5488ca3b50a60bc761"

def set_up_spotipy(database = 'spotify_api.db', j_file = 'artist_genres.json'):
    client_id = 'b3476765b11a4d5488ca3b50a60bc761'
    client_secret = '39083a77029242c5aff702ce8d132ddf'



# http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
# https://api.spotify.com/v1/artists/b3476765b11a4d5488ca3b50a60bc761/albums?
list_of_artist = ['Taylor Swfift', 'Nelly']

for artist in list_of_artist:
    para = {
        "q": artist,
        "type": "artist",
        "limit": "5"
    }
    #  headers=headers
    r = requests.get(searchUrl, params=para)
    json_data = json.loads(r.text)
    print(json_data)

    # if artist == json_data['artists']['items'][0]['name']:
    #     tup = (json_data['artists']['items'][0]['name'], json_data['artists']['items'][0]['id'])

    #     artistId_lst.append(tup)


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
    
    # 'http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6'
    

    request_url = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
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

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)



