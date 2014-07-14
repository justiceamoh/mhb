from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup


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
        lyrics = s.split('!\n')
        for i in lyrics:
            a += i+'\n\n'
        lyrics = a
    else:
        lyrics = '__'

           
    return lyrics

a =''
for i in range(1042):
    try:
        f = open('../data/'+str(i)+'.mhb')
        l = f.readlines()
        if l[3]== '__':  
            print i
            # break
            soup = make_soup(l[0].rstrip())     
            a = get_lyrics(soup)            
            f.flush()
            f.close()
	    h = open('../data/'+str(i)+'.mhb', 'a')
	    h. write(a.encode('utf8').decode('ascii','ignore'))
            h.flush()
            h.close()
    except:
        continue


