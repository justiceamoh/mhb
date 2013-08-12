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


def get_titles(entries):
    n = 0  
    titles = []
    errList = []        #records position of titles with errors
    for hymn in entries.findAll('a'):        
        if hymn.string == None:
            errList.append(n)
            titles.append('__')            
        else:            
            titles.append(hymn.string)
        n += 1        
    return (titles, errList)


def get_urls(entries):    
    url = [BASE_URL + hymn.get('href')[3:] for hymn in entries.findAll('a')]
##    url = [BASE_URL+i[3:] for i in url]    
    return url

    
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
    titles = []             # list contain the title each hymn
    urls = []
    authors = []    
    errors = []
    for line in lines:        
        soup = make_soup(line.rstrip())
        entries = soup.find("div","single-entry")
        (T,errCount) = get_titles(entries) 
        titles.append(T)
        urls.append(get_urls(entries))
        errors.append(errCount)
##        lyrics.append([get_lyrics(x) for x in urls[-1][:2]])
    return (titles,urls,errors)#,author)
    
   # return str(lyrics[0].encode('utf8').decode('ascii','ignore'))

(titles,urls,errors) = handler()
##whn writing to file encode as ascii

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

f.flush()
f.close()
h.flush()
h.close()
