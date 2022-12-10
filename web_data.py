from xml.sax import parseString
from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import unittest
import string
import sys
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# Your name: Debby Chung
# Your student id: 24199350
# Your email: debchung@umich.edu
# List who you have worked with on this project: Dylan Siewert
    

# Task 2: Look at the Get the URL that links to webpage of universities with Olympic medal wins
# search for the url in the University of Michgian wikipedia page (in the third pargraph of the intro)
# HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
def get_data_from_url(soup, cur, conn, num):
    data_url = []
    
    #findall of container
    section = soup.find('section', class_='mf-section-2')
    td_list = section.find_all('td')

    for item in range(len(td_list)):
        #country
        if item == 1:
            country = str(td_list[item].text)
            country = country.split()[0]
            print(country)
        #artist
        elif item == 2:
            artist = str(td_list[item].text)
            artist = artist.split()[0]
            print(artist)
        #weeks
        elif item == 3:
            weeks = int(td_list[item].text)
            print(weeks)
        else:
            continue
        
        #cur.execute("INSERT OR IGNORE INTO BillboardHot100 (song_title, artist_name, weeks_at_no_1) VALUES (?,?,?)",(country, artist, weeks))


def main():

    # Create table
    conn = sqlite3.connect('music.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS BillboardHot100 (song_title TEXT PRIMARY KEY, artist_name TEXT, genre TEXT, country TEXT, year INTEGER)')

    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this
    for num in [1982, 1992, 2002, 2012, 2022]:
        url = f'https://en.m.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_{num}' 
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        get_data_from_url(soup, cur, conn, num)

    #Call the functions getLink(soup) and getAdmissionsInfo2019(soup) on your soup object.
    # getLink(soup)
    # getAdmissionsInfo2019(soup)

#class TestAllMethods(unittest.TestCase):
    # def setUp(self):
    #     self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    # def test_link_nobel_laureates(self):
    #     self.assertEqual(getLink(self.soup), 'https://en.wikipedia.org/wiki/List_of_American_universities_with_Olympic_medals')


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)