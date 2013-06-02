mhb
===
Author: Justice Amoh
Date: June 2, 2013
Description: Methodist Hymn Book android app and libraries

Source Description
==================

./mhbformat.py 
python script to reformat hymn webpages to .mhb file format.
input: ./data/[mhb number]  
output: ./data/[mhb number].mhb

./hymnscraper.py
python script for scraping url's for hymns by title.
input: mhb_list.txt, url_list.txt.
output: ./data/[mhb number]


./url_list.txt
text file containing list of websites to search for hymns

./mhb_list.txt
text file containing titles and mhb numbers of hymns to be scrapped

./data
folder containing all formatted mhb files


