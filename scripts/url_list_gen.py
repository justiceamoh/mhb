"""
    This script automatically generates url_list.txt
"""
import string

def url_list_gen():
    alphabet = string.ascii_lowercase;
    alphabet = alphabet[:23] + 'yz' # no hymn begins with x

    urls = ['http://cyberhymnal.org/ttl/ttl-'+str(i)+'.htm' for i in alphabet]

    f = open('../url_list.txt','w')
    for i in urls:
        f.write(i+'\n')

url_list_gen()
