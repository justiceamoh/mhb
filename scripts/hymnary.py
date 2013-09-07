from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup

def make_soup(url):
    try:
        html = urlopen(url).read()
        return BeautifulSoup(html)
    except HTTPError:
##        print "Connection lost!"
        return None
##        exit(1)
    except URLError:
        print "Url not found..."
        return None
##        exit(1)

# soup = make_soup('http://www.hymnary.org/text/abide_among_us_with_thy_grace')


class hymn:
    def __init__(self,no,url):
        self.url = url
        self.no = no        
        try:
            self.soup = make_soup(url).find('div',typeof='CreativeWork') 
            self.title = self.soup.find('h2',id='authority_first_line')
            self.author = self.soup.findAll('a',href='#Author')[1]
            self.lyrics = self.soup.find('div','authority_columns').children
        except:
            self.no = 0 # error code...
            print url
            print 'error code'
        

    def get_url(self):
        return self.url
    
    def get_title(self):
        return self.title.text
    
    def get_author(self):
        return self.author.text
        
    def get_lyrics(self):
            s = ''
            for i in self.lyrics:
                s += i.text+'\n\n'        
            return s
      

# def handler():
e = open('../errors.txt')
er = e.readlines()
errors=[]
for i in er:
    errors.append(i.rstrip())

BASE_URL = 'http://www.hymnary.org/text/'
clean = []
for i in errors:    
    if len(i[4:])>40:
        n = hymn(i[:3], BASE_URL+i[4:40].replace(' ','_'))
    else:
        n = hymn(i[:3], BASE_URL+i[4:].replace(' ','_'))

    if n.no == 0:
        continue

    f = open('../data/' + str(n.no.replace(' ',''))+'.mhb','w')
    f.write(n.get_url() +'\n' + n.get_title() +'\n' + n.get_author() + '\n\n' + n.get_lyrics())
    f.flush()
    f.close()

    clean.append(i)
