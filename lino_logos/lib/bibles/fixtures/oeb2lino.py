# -*- coding: UTF-8 -*-
## Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""

not finished. usfm is more complex than i thought.
what about concordances?

Read .usfm files from
`Russell Allen's Open English Bible
<https://github.com/openenglishbible/Open-English-Bible>`_



"""

from urlparse import urlparse
import requests
from bs4 import BeautifulSoup


def tostring(x):
    return ' '.join(x.stripped_strings)


def load_book(url):
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    #~ for section in soup.find_all('span',attrs={"class": "h3"}):
    for section in soup.find_all('a'):
        print(section)


def extract(book_ref, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for book in soup.find_all('div', attrs={"class": "listitem"}):
        #~ print book
        for a in book.h3.find_all('a'):
            #~ print a['href']
            load_book(base_url + a['href'])
            #~ print tostring(a)
        #~ cells = row.find_all('td')
        #~ if len(cells) == 8:
        #~ fr=tostring(cells[0])
        #~ nl=tostring(cells[1])
        #~ province=tostring(cells[2])
        #~ type=tostring(cells[3])
        #~ print fr, nl, province,type
        #~ elif len(cells) == 0:
        #~ pass
        #~ else:
        #~ raise Exception("Found row %s with %d cells"  % (cells,len(cells)))


if __name__ == '__main__':

    extract(
        "genesis",
        "https://raw.github.com/openenglishbible/Open-English-Bible/master/final-usfm/cth/01-Genesis.usfm"
    )
