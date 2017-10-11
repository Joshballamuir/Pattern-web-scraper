import pattern_web_scraper_functions

#AIM TO MAKE ALL VARIABLES DISPOSABLE!
first_name_list = []
last_name_list = []
full_name_list = []
synonyms_1 = [
    'chief executive officer','ceo',
    'director','head of company',
    'chairman','founder'
    ]
synonyms_2 = [
    'chief financial officer','cfo',
    'head of finance','accounts',
    'head of accounts','treasurer'
    ]
synonyms_3 = [
    'chief technology officer','cto',
    'technology director','head of technology',
    'development','chief of technology'
    ]
    #synonym lists to be plugged into programme at user's request
prep = [
    'J:','%'
    ]
prep1 = [
    '">','"><b>','\d+',
    '</b>','<b>'
    ]
idword = '|+'
idword2 = '3Dcache'
company_name = input("Enter company name ")
employee_position = input("Enter employee position ")
url = ('https://www.google.co.uk/search?q='+company_name)
urls = [
    url+'+'+synonyms[0],url+'+'+synonyms[0]+'+&start=10',
    url+'+'+synonyms[0]+'+&start=20',url+'+'+synonyms[1],
    url+'+'+synonyms[1]+'+&start=10',url+'+companies+house+officers'
    ]
urls1 = [
    ]
blacklist = synonyms_1+synonyms_2+synonyms_3+company_name+[
         '&','#',':',';','(',')','group','technologies','direct','careers',
         'tooshort','profiles', 'accountant', 'jobs', 'united', 'kingdom',
         'international', 'plc','lp', 'linkedin','ltd','limited','...',
         '/script','/body','director','finance','cfo','chief','financial',
         'officer','controller','accounts','manager','management','fd',
         'presidential','articles,','salaries','telecom','solutions',
         'area','the','head','of','uk'
         ]
         #blacklist for words frequently appearing where names are found in search results
wordlist_generator(
    new_name_finder_functions.format_for_keyword(new_name_finder_functions.linkedin_google_search)).split()
name_final(
    name_compilation(site_finder)
    )
first_name_list.append(first_name)
last_name_list.append(last_name)
full_name_list.append(full_name)
print(director1)
print(director2)
#gen_name(new_name)

#upload to github
#separate all variables from functions. Variables must be changeable - can bridge this into machine learning!!
#use synonyms included here on website bot to prove concept of machine learning
#integrate into emails using files and dependencies as have began to here!
#implement machine learning for pattern finding
