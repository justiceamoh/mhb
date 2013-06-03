#!/usr/bin/python

from urllib2 import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "http://cyberhymnal.org/"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_category_hymns(category_url):
    soup = make_soup(category_url);
    category = soup.title.string
    entries = soup.find("div","single-entry")
    title = [hymn.string for hymn in entries.findAll("a")]

    url = [BASE_URL + hymn.get('href') for hymn in entries.findAll("a")]
    url = [hymn.split('../')[0] + hymn.split('../')[1] for hymn in url]

    data=[]
    data.append(title)
    data.append(url)

    output=dict()
    output[category[2:3]]=data
    return output

category = get_category_hymns("http://cyberhymnal.org/ttl/ttl-a.htm")
# pprint(titles)
pprint(category)
