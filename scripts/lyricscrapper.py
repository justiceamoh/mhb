from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup

f = open('../titleUrls.txt')
h = open('../titles.txt')
urlLines = f.readlines()
titleLines = h.readlines()
l = []
url = []
x=0
for line in urlLines:
    try:
        soup = BeautifulSoup(urlopen(line.rstrip()).read())
        lyrics = soup.find('div','lyrics')
        s = ""
        if lyrics != None:
            for i in lyrics.strings: # i is one verse
                if i == '\n':
                    s +='\n'
                s += i
            lyrics = s[1:]
        else:
            lyrics = '__'
        l.append(lyrics)
    except HTTPError:
        l.append('___No Lyrics found on site__')
    except URLError:
        l.append('Server is not resoponding; chk ur connection')
        
g = open('../lyrics.txt','w')
i=0
for title in titleLines:
        g.write(title + l[i]+'\n\n')
        i+= 1

f.flush()
g.flush()
h.flush()
f.close()
g.close()
h.close()
