#!/usr/bin/python

from urllib2 import urlopen
from bs4 import BeautifulSoup
from time import sleep
from pprint import pprint
from string import maketrans
from string import punctuation

BASE_URL = "http://cyberhymnal.org/"
URLS_FILE = "url_list.txt"

hymnGlobal = ""
def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)


def get_titles():
    global entries
    global count
    n = 0
    title = []
    for hymn in entries.findAll('a'):
        n += 1
        if hymn.string == None:
            count = n
            continue
        title.append(hymn.string)    
    titles= []
    for i in range(len(title)):
        titles.append(title[i])        
    return titles


def get_urls():
    global entries
    global count
    n = 0    
    url = [] 
    for hymn in entries.findAll('a'):
        n+=1
        if n == count:
            continue
        url.append(hymn.get('href'))
    newUrl = []
    for i in url[:]:
        newUrl.append(BASE_URL+i[3:])
    return newUrl

    
def get_lyrics(url):
    soup = make_soup(url)
    lyrics = soup.find('div','lyrics')
    s = ""
    for i in lyrics.strings:
        if i[:1] != '\r':
            s +='\n'
        s += i
    lyrics = s[2:]
    return lyrics

##def get_authors(url):
    
    

def handler():    
    f = open(URLS_FILE)
    lines = f.readlines()

    lyrics = []             # holds the lyrics of each hymn
    titles = []           # list contain the title each hymn
    urls = []
    authors = []
    global entries,count
    count = 0
    for line in lines:
        soup = make_soup(line.rstrip())
        entries = soup.find("div","single-entry")
        titles.append(get_titles()) ##whn writing to file encode as ascii
        urls.append(get_urls())
        count = 0
##    lyrics.append([get_lyrics(x) for x in urls[-1][:2]])
    return (titles,urls)#,lyrics,author)
    
   # return str(lyrics[0].encode('utf8').decode('ascii','ignore'))

(titles,urls) = handler()

f = open('titles.txt','w')
h = open('titleUrls.txt','w')
j=k=0
y=""
for i in titles:
    for x in i:
        x = str(x.encode('utf8').decode('ascii','ignore'))
        y = str(urls[j][k].encode('utf8').decode('ascii','ignore'))
        f.write(x+'\n')
        h.write(y+'\n')
        k += 1
    j += 1
    k=0

f.fush()
f.close()
h.flush
h.close()

