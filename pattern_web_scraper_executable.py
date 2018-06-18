import pattern_web_scraper_functions

google_pattern = [
    'J:','%'
    ]
google_pattern1 = [
    '">','"><b>','\d+',
    '</b>','<b>'
    ]
#google pattern words to sift through data

linkedin_pattern = '|+'
linkedin_pattern1 = '3Dcache'
#linkedin pattern words to sift through data

subject = input("Enter subject (e.g company name) ")
synonyms = input("Enter location of your synonyms csv file ")
blacklist = subject+synonyms+input("Enter blacklist csv ")

google_page1 = ('https://www.google.co.uk/search?q='+subject)
google_page2 = google_page1+'+&start=10'
google_page3 = google_page1+'+&start=20'



#print(director1)
#print(director2) #output result

#AIM TO MAKE ALL VARIABLES DISPOSABLE!
#integrate into emails using files and dependencies as have began to here!
#synonym lists to be plugged into programme at user's request. Soon automate with thesaurus programme
#automate pattern detection
