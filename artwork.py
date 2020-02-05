from urllib.request import urlopen
import json

def homepage():
    file = urlopen('http://142.93.129.123:32823/NowOnAir.xml').read()
    file = file.decode()
    for item in file.split("\n"):
        if "Artist name" in item:
            artistName = (item.strip())[14:][:-10]
            print(artistName)
    for item in file.split("\n"):
        if "Song title" in item:
            songTitle =  (item.strip())[13:][:-2]
            print(songTitle)

homepage()

import os
import sys
import apis

class AlbumArtGrabber(object):
    def __init__(self, root_directory='.', cover_name='cover.'):
        self.last_fm = apis.LastFMAlbumArt(
            key='8c95f92a46b2dedce897ebbd46e6e575',
            secret='93444c81db008d7de67fa7c19900429f'
        )
        self.itunes = apis.iTunesAlbumArt()
        self.root_directory = root_directory
        self.cover_name = cover_name
        self.image_exts = [
            'jpg',
            'gif',
            'png'
        ]
        self.music_exts = [
            'mp3',
            'flac'
        ]
    def _get_album_art_url(self, artist, album):
        pic_url = self.itunes.find_art(artist, album)
        if not pic_url:
            pic_url = self.last_fm.find_art(artist, album)
        return pic_url

if __name__ == '__main__':
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = '.'
    grabber = AlbumArtGrabber(root_directory=directory)
    grabber.find_albums()