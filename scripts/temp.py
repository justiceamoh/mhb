from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup


m = open('../mhb_list.txt')
mhb = m.readlines()
mhbList = []
for i in mhb:
    mhbList.append(i[4:].rstrip().lower())


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

def get_lyrics(soup):
    s = ''  
    lyrics = soup.find('div','lyrics')
    a = ""
    if lyrics != None:
        for i in lyrics.strings: # i is one verse or esc sequence whn there's a paragraph
            if i == '\n':
                s +='\n'
            s += i
        lyrics = s[1:]
    elif  soup.find('td','lyrics') != None:
        lyrics = soup.find('td','lyrics')
        for i in lyrics.strings:
            s += i
        lyrics = s.split('.\n')
        for i in lyrics:
            a += i+'\n\n'
        lyrics = a
    else:
        lyrics = '__'
           
    return lyrics

def get_authors(soup):
    author = soup.findAll('meta')[1]['content'][:]
    author = author.split(',',1)[0]
    return author

url = 'http://cyberhymnal.org/htm/g/b/g/gbgohigh.htm'
title = 'Glory be to God on high'.lower()
try:
    soup = make_soup(url)
    lyrics = get_lyrics(soup)
    authors = get_authors(soup)              
except HTTPError:
    lyrics = '___Broken url__/n/n'
    authors = ' '
except URLError:
    lyrics = 'Internet connection Error/n/n'
    authors = ' '


output = open('../data/'+ str(mhb[mhbList.index(title)][:3])+'.mhb', 'w')
a = authors.encode('utf8').decode('ascii','ignore')
l = lyrics.encode('utf8').decode('ascii','ignore')
output.write(url+'\n'+title.title()+'\n'+ a +'\n' + l)

output.flush()
output.close()