#!/usr/bin/python

from urllib2 import urlopen
from bs4 import BeautifulSoup
from time import sleep
from pprint import pprint
from string import maketrans
from string import punctuation

BASE_URL = "http://cyberhymnal.org/"
URLS_FILE = "url_list.txt"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_category_hymns(category_url):
    soup = make_soup(category_url);
    category = soup.title.string
    entries = soup.find("div","single-entry")

    title = [hymn.string for hymn in entries.findAll("a")]
    title = [x.lower() for x in title]
    title = [x.translate(maketrans("",""), punctuation) for x in title]

    url = [BASE_URL + hymn.get('href') for hymn in entries.findAll("a")]
    url = [hymn.split('../')[0] + hymn.split('../')[1] for hymn in url]

    data=[]
    data.append(title)
    data.append(url)

    output=dict()
    output[category[2:3]]=data
    return output



f = open("url_list.txt")
lines = f.readlines()

all_hymns = dict()

for line in lines:
    new = get_category_hymns(line.rstrip())
    all_hymns.update(new)
    sleep(1)



pprint(all_hymns)
