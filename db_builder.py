#!/usr/bin/python
# Author: Justice Amoh
# Description: Script to build sqlite3 database out of hymn files (.mhb)

import sqlite3, glob, os

database =sqlite3.connect("mhb.db")
cursor = database.cursor()

#creating a table
cursor.execute("""CREATE TABLE a 
	(mhb integer, title text, author text, hymn text)""")

os.chdir("data")
for ifile in glob.glob("*.mhb"):
	with open(ifile) as f:
		url=f.readline().rstrip('\n')
		title=f.readline().rstrip('\n')
		author=f.readline().rstrip('\n')
		dump=f.readline()
		hymn=f.read()

		sql = "INSERT INTO a VALUES (?, ?, ?, ?)" 
		values = [ifile.rstrip('.mhb'),title,author,buffer(hymn)]
 		cursor.execute(sql,values)


# query: display all of table a
# cursor.execute("select * from a")
# for row in cursor:
#     print row 		

#save updates and close database
database.commit()
database.close()
