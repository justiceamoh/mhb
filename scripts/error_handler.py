from time import sleep

##get titles
t = open('titles.txt')
t1 = open('titles1.txt')
titles = t.readlines()
titles1 = t1.readlines()
## get the hymnos and urls
m = open('mhb_list.txt')
m1 = m.readlines()

title = []       # this list ties up each titles&urls
mhbList = []    # contains only the titles
hymnNos = []    # contains only the hymn numbers
errors = []
title1 = []
# separate the titles from their hymn nos.
for i in m1:
    mhbList.append(i[4:].lower().rstrip())

for i in titles:
    title.append(i.rstrip().lower())
    title1.append(i.rstrip().lower())

for i in mhbList:
	if i not in title:
		errors.append(i)

errors.sort()

##for i in range(25):
##	print errors[i]
