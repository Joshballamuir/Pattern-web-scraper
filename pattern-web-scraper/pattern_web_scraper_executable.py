import pattern_web_scraper_functions
#AIM TO MAKE ALL VARIABLES DISPOSABLE!
#integrate into emails using files and dependencies as have began to here!
#synonym lists to be plugged into programme at user's request. Soon automate with thesaurus programme

google_pattern = [
    'J:','%'
    ]
google_pattern1 = [
    '">','"><b>','\d+',
    '</b>','<b>'
    ]
linkedin_pattern = '|+'
linkedin_pattern1 = '3Dcache'#pattern words to sift through data. will automate finding using machine learning

subject = input("Enter subject (e.g company name) ")
synonyms = input("Enter location of your synonyms csv file ")
blacklist = subject+synonyms+input("Enter blacklist csv ")

google_page1 = ('https://www.google.co.uk/search?q='+subject)
google_page2 = google_page1+'+&start=10'
google_page3 = google_page1+'+&start=20'

slug(googlelinkedinurlsetc) #format url

wordlist_generator(
    new_name_finder_functions.format_for_keyword(new_name_finder_functions.linkedin_google_search)).split() # #generate words

word_final(
    name_compilation(site_finder)
    ) #determine best match

first_name_list.append(first_name)
last_name_list.append(last_name)
full_name_list.append(full_name) #filter best match

print(director1)
print(director2) #output result
