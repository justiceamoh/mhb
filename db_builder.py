#!/usr/bin/python
# Author: Justice Amoh
# Description: Script to build sqlite3 database out of hymn files (.mhb)

import sqlite3, glob, os

# conn =sqlite3.connect("mhb.db")
# cursor = conn.cursor()

#creating a table
# cursor.execute("""CREATE TABLE a (mhb integer, title text, author text, hymn text)""")

os.chdir("data")
for files in glob.glob("*.mhb"):
	with open(files) as f:
		url=f.readline().rstrip('\n')
		title=f.readline().rstrip('\n')
		author=f.readline().rstrip('\n')
		dump=f.readline()
		hymn=f.read()

	print url
	print title
	print hymn
	print "\n\n\n"
# with open ('datafile') as f:
#     data=f.read()

# sql = "INSERT INTO a VALUES (511, 'Begone Unbelief', 'John Newton', '?')" 

# cursor.execute(sql,[buffer(data)])
# conn.commit()





# import glob
# import os
# os.chdir("/mydir")
# for files in glob.glob("*.txt"):
#     print files