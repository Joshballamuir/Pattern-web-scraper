import collections
import re
import requests
import ssl
import sys
from pattern_web_scraper_test_suite import blacklist,synonyms_1,synonyms_2,synonyms_3,url
#from pattern_web_scraper_executable import blacklist,synonyms_1,synonyms_2,synonyms_3,url

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

def slug(slug_item):
    return(re.sub(r' ','+',re.sub(r'&','and',slug_item)).lower())
#converts item to name to a valid google search format
def gen_name(new_name):
    first_name = new_name[0]
    try:
        last_name = new_name[1]
    except IndexError:
        return('Not found')
    full_name = first_name+' '+last_name
    for i in blacklist:
        if i in full_name:
            return('Not found')
        else:
            continue
    return(first_name,last_name,full_name)
#generates list of names from descriptions of linkedin search results checked against blacklist
def linkedin_google_search(employee):
    url_list = []
    if employee in synonyms_1:
        synonyms = synonyms_1
    elif employee in synonyms_2:
        synonyms = synonyms_2
    elif employee in synonyms_3:
        synonyms = synonyms_3
    for i in synonyms:
        url_list.append(url+i+'+linkedin')
    return(url_list)
#generates start urls
###TESTED FUNCTIONS###

def gen_html_text(urls,idword):
    for i in urls:
        session.mount(site,MyAdapter())
        try:
            html_dump = html_dump + session.get(i,allow_redirects=False).text
        except(
            requests.exceptions.SSLError,requests.exceptions.ConnectionError,
            requests.packages.urllib3.exceptions.NewConnectionError,
            requests.packages.urllib3.exceptions.MaxRetryError
            ) as e:
                continue
    return(html_dump)
#generates the html text
def html_dump_prep(html_dump):
    re.sub(non_letters.sub(' ',html_dump).translate(non_bmp_map).lower())
    for i in prep:
        html_dump = re.sub(r+i,' ',html_dump)
    return(html_dump)
#preps the html dump for the finding function
def word_finder(html_dump):
    found = []
    before_idword,idword,after_idword = html_dump.partition(idword)
    loop = 1
    while loop == 1:
        found.append(after_idword2.split()[1])
        try:
            before_idword,idword,after_idword = after_idword.partition(idword)
        except ValueError:
            return(found)
        #found = urls for 3dcache
        #find new idword to replace '|+<b>' so it works for AFTER keyword, rather than before - also find removables and put into a list!
#generates a list of words from data by iterating through a found keyword
def name_compilation(first_name_list,html_dump):
    for i in first_name_list:
        #consider adding points for last_name
        if i in html_dump:
            final_names.append(list(re.findall('\\b'+i+'\\b',html_dump)))#not showing all names?#repeat for surname?
    final_names = (Counter(final_names).most_common(2))
    return(final_names)
#compiles list of names found and narrows it down to 2 final names
def name_final(final_names):
    try:
        for i in final_names:
            if i in full_name_list:
                print(i+[i]).title()
    except IndexError:
        print('Not found')
#finalises and reformats 2 names to be returned
###UNTESTED FUNCTIONS###
