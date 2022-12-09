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
def get_data_from_url(soup, cur, conn):

    #findall of container
    tr_list = soup.find_all('table', class_='wikitable plainrowheaders')[1]
    for td in range(1, len(tr_list)):
        #country
        title = str(td.find("td")[1].text)

        #artist
        artist = str(td.find("td")[2].text)

        #weeks
        weeks = str(td.find("td")[3].text)

        cur.execute("INSERT OR IGNORE INTO BillboardHot100 (song_title, artist_name, weeks_at_no_1) VALUES (?,?,?)",(title, artist, weeks))

    # return 'https://en.wikipedia.org'+a_tag.get('href')

# Task 3: Get the details from the box titled "College/school founding". Get all the college/school names and the year they were
# founded and organize the same into key-value pairs.

# def getAdmissionsInfo2019(soup):
#     table_tag = soup.find('table',class_='toccolours')
#     tr_list = table_tag.find_all('tr')
#     d = {}
#     for tr_tag in tr_list[1:]:
#         td_list = tr_tag.find_all('td')
#         school_name = td_list[0].text.strip()
#         found_year = td_list[1].text.strip()
#         d[school_name] = found_year
#     return d


def main():

    # Create table
    conn = sqlite3.connect('music.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS BillboardHot100 (song_title TEXT PRIMARY KEY, artist_name TEXT, genre TEXT, country TEXT, weeks_at_no_1 INTEGER)')

    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this
    for num in [1982, 2002, 2022]:
        url = f'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_{num}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        get_data_from_url(soup, cur, conn)

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