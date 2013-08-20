from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup
# from time import sleep

BASE_URL = "http://cyberhymnal.org/"


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

 
def get_lyrics(soup):
    s = ''  
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
           
    return lyrics           


def get_authors(soup):
    author = soup.findAll('meta')[1]['content'][:]
    author = author.split(',',1)[0]
    return author


##get titles
t = open('../titles.txt')
titles = t.readlines()
## get the titles' urls
u = open('../titleUrls.txt')
urls = u.readlines()
## get the hymnos and urls
m = open('../mhb_list.txt')
m1 = m.readlines()

tie = []        # this list ties up each titles&urls
mhbList = []    # contains only the titles
hymnNos = []    # contains only the hymn numbers
resultDict = {} # dictionary that holds titles that tallied and their hymn nos.

# separate the titles from their hymn nos.
for i in m1:
    mhbList.append(i[4:].lower())
    hymnNos.append(int(i[:4].strip()))

##wrap each url and title in a tuple and store the result in a list
for i in range(len(titles)):
    wrap = (titles[i],urls[i]) 
    tie.append(wrap)

#compare titles to knw which ones tally
for i in tie:
    if i[0].lower() in mhbList:
        k = mhbList.index(i[0].lower())
        resultDict[hymnNos[k]] = (i[0].lower().title(), i[1])        
        mhbList[k] = '' #tracks titles with no errors
        ## the 0s are more than one! chk dat latter

def handler(resutlDict):
    urls = []
    lyrics = []
    authors = []
    # k=0
    for i in resultDict.values():
        urls.append(i[1])
    for i in urls:
        # if k<=2:
        try:
            soup = make_soup(i)
            lyrics.append(get_lyrics(soup))
            authors.append(get_authors(soup))                
        except HTTPError:
            lyrics.append('___Broken url__/n/n')
            authors.append(' ')
        except URLError:
            lyrics.append('Internet connection Error/n/n')
            authors.append(' ')
            # k += 2
    return (authors,lyrics)

authors, lyrics = handler(resultDict)


for i in range(len(resultDict)):
    output = open('../data/'+ str(resultDict.keys()[i]) + '.mhb', 'w')
    a = authors[i].encode('utf8').decode('ascii','ignore')
    l = lyrics[i].encode('utf8').decode('ascii','ignore')
    output.write(resultDict.values()[i][1]+resultDict.values()[i][0]+ a +'\n' + l)
    output.flush()
    output.close()

t.flush()
t.close()
m.flush()
m.close()
u.flush()
u.close()
