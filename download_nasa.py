#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
*********************************************
 Nasa's picture of the day since 1995.
 by Cecil Woebker (http://cwoebker.com)
*********************************************
 Usage:
 $ ./apod.py
 Saves all pictures from Nasa's picture of the day archive to the current directory.
"""

import os

import _pickle as pickle
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

from clint.textui import progress, puts, colored

ROOT_URL = 'http://apod.nasa.gov/apod/'

def load():
    puts("Loading archive...")
    urls = []
    data = urlopen(ROOT_URL + 'archivepix.html').read()
    puts("Opening archive...")
    soup = BeautifulSoup(data, 'lxml')
    results = soup.find('b').findAll('a')
    for result in progress.bar(results):
        urls.append(result['href'])
    puts(colored.green("Found %d links." % len(urls)))
    return urls

def getPhotos(urls, thumbs=False):
    puts("Locating Photos...")
    photos = {}
    typeErrorCount = 0
    keyErrorCount = 0
    urlErrorCount = 0
    for url in progress.bar(urls):
        try:
            data = urlopen(ROOT_URL + url).read()
            soup = BeautifulSoup(data, 'lxml')
            result = soup.find('img')
            if result is None:
                typeErrorCount += 1
                continue
            if thumbs:
                photos[url] = result['src']
            else:
                photos[url] = result.parent['href']
        except TypeError:
            typeErrorCount += 1
        except KeyError:
            keyErrorCount += 1
        except URLError:
            urlErrorCount += 1
    puts(colored.green("Found %d photos." % len(photos.values())))
    puts(colored.red("URL Error Count: %d" % urlErrorCount))
    puts(colored.red("Key Error Count: %d" % keyErrorCount))
    puts(colored.red("Type Error Count: %d" % typeErrorCount))
    with open('photos.pkl', 'wb') as output:
        pickle.dump(photos, output, pickle.HIGHEST_PROTOCOL)
    return photos


def downloadPhoto(folder, photo):
    try:
        u = urlopen(photo)
        localFile = open(os.path.join(folder, photo.split('/')[-1]), "wb")
        localFile.write(u.read())
        localFile.close()
        u.close()
    except HTTPError:
        puts(colored.red("HTTPError - 404"))


def main():
    print(__doc__)
    urls = load()
    photos = getPhotos(urls)
    puts("--------------")
    puts(colored.yellow("Downloading..."))
    puts("--------------")
    for key in progress.bar(photos.keys()):
        name = key.split('.')[0]
        parts = [name[i:i+2] for i in range(0, len(name), 2)]
        print(parts[1]+parts[2]+parts[3])
        folder = os.path.join(parts[1], parts[2], parts[3])
        if not os.path.exists(folder):
            os.makedirs(folder)
        item = ROOT_URL + photos[key]
        downloadPhoto(folder, item)
        #puts("%s done." % key)
    puts(colored.green("Finished."))


if __name__ == "__main__":
    main()