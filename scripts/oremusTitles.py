from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup
import string

def make_soup(url):
    # try:
    html = urlopen(url).read()
    return BeautifulSoup(html)
    # except HTTPError:
    #     return None
    # except URLError:        
    #     return None
title = ''
for i in string.ascii_lowercase:
	try:
		soup = make_soup('http://www.oremus.org/hymnal/'+str(i)+'/'+str(i)+'.html')
		p = soup.find('p')
		t = p.text[:-2275]
		title += t.replace('\r\n',' ')
	except:
		continue

f = open('../oremTitles.txt','w')
titles = title.split('\n')

for i in titles:
	f.write(i.encode('utf8').decode('ascii','ignore')+'\n')

f.flush()
f.close()