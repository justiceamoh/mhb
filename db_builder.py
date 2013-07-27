#!/usr/bin/python
# Author: Justice Amoh
# Description: Script to build sqlite3 database out of hymn files (.mhb)

import sqlite3

conn =sqlite3.connect("mhb.db")
cursor = conn.cursor()

#creating a table
cursor.execute("""CREATE TABLE a (mhb integer, title text, author text, hymn text)""")

with open ('datafile') as f:
    data=f.read()

sql = "INSERT INTO a VALUES (511, 'Begone Unbelief', 'John Newton', '?')" 

cursor.execute(sql,[buffer(data)])
conn.commit()