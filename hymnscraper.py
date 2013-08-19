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
    return url
 
def get_lyrics(urls):
    s = ''
    l = []    
    for url in urls:#######New code additions
            try:
                soup = make_soup(url)
                lyrics = soup.find('div','lyrics')
                s = ""
                if lyrics != None:
                    for i in lyrics.strings: # i is one verse or esc sequence whn there's a paragraph
                        if i == '\n':
                            s +='\n'
                        s += i
                    lyrics = s[1:]
                else:
                    lyrics = '__'
                l.append(lyrics)
            except HTTPError:
                l.append('___Broken url: No Lyrics found on site__')
    return l            ######New code additions

    
def handler():    
    f = open(URLS_FILE)
    lines = f.readlines()

    lyrics = []             # holds the lyrics of each hymn
    titles = []             # list contain the title each hymn
    urls = []
    authors = []    
    errors = []             #some titles have 'bad' markup in their names
    for line in lines:        
        soup = make_soup(line.rstrip())
        entries = soup.find("div","single-entry")
        (T,errCount) = get_titles(entries) 
        titles.append(T)
        urls.append(get_urls(entries))
        lyrics.append(get_lyrics(urls[-1])
##        authors.append(get_authors(urls[-1])        
        errors.append(errCount)
    return (titles,urls,lyrics,errors)


(titles,urls,lyrics,errors) = handler()

##whn writing to file encode as ascii
f = open('titles.txt','w')
##h = open('titleUrls.txt','w')
j=k=0
##y=""
for i in titles:
    for x in i:
        x = str(x.encode('utf8').decode('ascii','ignore'))        
        f.write(x+lyrics[j][k]+'\n\n')
##        h.write(y+'\n')
        k += 1
    j += 1
    k=0

f.flush()
f.close()
h.flush()
h.close()

