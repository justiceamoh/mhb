from time import sleep

##get titles
t = open('../titles.txt')
t1 = open('../titles1.txt')
titles = t.readlines()
titles1 = t1.readlines()
## get the hymnos and urls
m = open('../mhb_list.txt')
mhbList = m.readlines()

title = []       # this list ties up each titles&urls
# mhbList = []    # contains only the titles
hymnNos = []    # contains only the hymn numbers
errors = []
title1 = []
# separate the titles from their hymn nos.
# for i in m1:
#     mhbList.append(i[4:].lower().rstrip())

for i in titles:
    title.append(i.rstrip().lower())
    title1.append(i.rstrip().lower())

for i in mhbList:
	if i[4:].rstrip().lower() not in title:
		errors.append(i)

f = open('../errors1.txt', 'w')
for i in errors:
	f.write(i)

##for i in range(25):
##	print errors[i]
