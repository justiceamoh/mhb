mhb
===
Author: Justice Amoh
Date: June 2, 2013
Description: Methodist Hymn Book android app and libraries

Source Description
==================
./db_builder.py
python script to build an sqlite3 database (mhb.db) from all hymn files in ./data/. 
Output: mhb.db

./hymnscraper.py
python script for scraping url's for hymns by title. stores hymns as .mhb formats in ./data/ folder.
input: mhb_list.txt, url_list.txt.
output: ./data/[mhb number].mhb

./url_list.txt
text file containing list of websites to search for hymns

./mhb_list.txt
text file containing titles and mhb numbers of hymns to be scrapped

./mhb.db
sqlite3 database of hymns. 
column headers:
[ mhb(integer)     title(text)       author(text)      hymn(text) ]

./data
folder containing all formatted mhb files. 


.mhb format:
file name       = hymn mhb number
first line      = hymn url
second line     = hymn title
third line      = hymn author
remainder lines = hymn lyrics


