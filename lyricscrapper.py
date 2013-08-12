from urllib2 import urlopen
from bs4 import BeautifulSoup

BASE_URL = "http://cyberhymnal.org/"

f = open('titleUrls.txt')
h = open('titles.txt')
urlLines = f.readlines()
titleLines = h.readlines()
l = []
url = []
x=0
for line in urlLines:
    soup = BeautifulSoup(urlopen(line.rstrip()).read())
    lyrics = soup.find('div','lyrics')
    s = ""
    if lyrics != None:
        for i in lyrics.strings:
            if i[:1] != '\r':
                s +='\n'
            s += i
        lyrics = s[2:]
    else:
        lyrics = '__'
    l.append(lyrics.encode('utf8').decode('ascii','ignore'))
    

g = open('lyrics.txt','w')
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

        
