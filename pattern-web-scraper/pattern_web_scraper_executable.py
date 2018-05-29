import pattern_web_scraper_functions
import collections
import re
import requests
import ssl
import sys

session = requests.Session()
session.max_redirects = 20

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
non_letters = re.compile('[^a-zA-Z]')

class MyAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLSv1
            )

#AIM TO MAKE ALL VARIABLES DISPOSABLE!
#integrate into emails using files and dependencies as have began to here!
#synonym lists to be plugged into programme at user's request. Soon automate with thesaurus programme
#automate pattern detection

google_pattern = [
    'J:','%'
    ]
google_pattern1 = [
    '">','"><b>','\d+',
    '</b>','<b>'
    ]
linkedin_pattern = '|+'
linkedin_pattern1 = '3Dcache'#pattern words to sift through data

subject = input("Enter subject (e.g company name) ")
synonyms = input("Enter location of your synonyms csv file ")
blacklist = subject+synonyms+input("Enter blacklist csv ")

google_page1 = ('https://www.google.co.uk/search?q='+subject)
google_page2 = google_page1+'+&start=10'
google_page3 = google_page1+'+&start=20'

print(director1)
print(director2) #output result
