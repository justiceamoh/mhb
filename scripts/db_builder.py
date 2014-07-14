#!/usr/bin/python
# Author: Justice Amoh
# Description: Script to build sqlite2 database out of hymn files (.mhb)


import sqlite3, glob, codecs, os, sys, re



# Natural Order Sort Function 
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


database =sqlite3.connect("../db/mhb.db")
cursor = database.cursor()


#creating a table
cursor.execute('drop table if exists hymns')
cursor.execute("""CREATE VIRTUAL TABLE hymns USING fts3
	(_id integer primary key, title text, author text, url text, lyrics text)""")

#Sqlite Adjustments for use in android
cursor.execute('drop table if exists android_metadata')
cursor.execute("""CREATE TABLE "android_metadata" 
	("locale" TEXT DEFAULT 'en_US')""") 
cursor.execute("INSERT INTO android_metadata VALUES ('en_US')")


os.chdir("../data")
files = os.listdir(".")
files = natural_sort(files) 
for ifile in files:
	with codecs.open(ifile,"r","utf-8") as f:
		ifile=int(ifile.rstrip('.mhb'))
		url=f.readline().rstrip('\n')
		title=f.readline().rstrip('\n')
		author=f.readline().rstrip('\n')
		dump=f.readline()	

		#TODO temporary hack to read all of code
		lyrics=''
		temp=f.read()
		while(temp!=''):
			lyrics+=temp
			temp=f.read()

		# sql = "INSERT INTO a VALUES (?, ?, ?, ?)" 
		# values = [ifile.rstrip('.mhb'),title,author,url]

		sql = "INSERT INTO hymns VALUES (?, ?, ?, ?, ?)" 
		values = [ifile, title, author, url, lyrics]
 		cursor.execute(sql,values)


# query: display all of table a
# cursor.execute("select * from a")
# for row in cursor:
#     print row 		

#save updates and close database
database.commit()
database.close()
