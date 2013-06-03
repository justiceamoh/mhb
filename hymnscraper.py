#!/usr/bin/python

from urllib2 import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "http://cyberhymnal.org/ttl/ttl-a.htm"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_category_hymns(category_url):
    soup = make_soup(category_url);
    title = soup.title.string
    #edit title to get first two words

    entries = soup.find("div","single-entry")
    title = [hymn.string for hymn in entries.findAll("a")]
    # print title
    url = [BASE_URL + hymn.get('href') for hymn in entries.findAll("a")]
    return url
    # return {"category": category,
    # 	"hymn_title": titles,
    #     "hymn_url": urls}


titles = get_category_hymns("http://cyberhymnal.org/ttl/ttl-a.htm")
pprint(titles)