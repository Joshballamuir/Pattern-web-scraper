import unittest
import pattern_web_scraper_functions

#import from pattern_web_scraper_executable:
blacklist = [
         '&','#',':',';','(',')','group','technologies','direct','careers',
         'tooshort','profiles', 'accountant', 'jobs', 'united', 'kingdom',
         'international', 'plc','lp', 'linkedin','ltd','limited','...',
         '/script','/body','director','finance','cfo','chief','financial',
         'officer','controller','accounts','manager','management','fd',
         'presidential','articles','salaries','telecom','solutions',
         'area','the','head','of','uk'
         ]
         #blacklist for words frequently appearing where names are found in search results
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
url = ('https://www.google.co.uk/search?q=test')

class pattern_web_scraper_functions_TestCase(unittest.TestCase):
    """Tests for `new_name_finder_functions.py`."""
#slug
    def test_is_company_name_lower(self):
        """Does it convert to lower case?"""
        self.assertEqual('hello',pattern_web_scraper_functions.slug('hELlO'))

    def test_is_company_name_spaced(self):
        """Does it replace ' ' with '+'?"""
        self.assertEqual('h+e+l+l+o',pattern_web_scraper_functions.slug('h e l l o'))
    def test_is_company_name_and(self):
        """Does it replace '&'' with 'and'?"""
        self.assertEqual('and',pattern_web_scraper_functions.slug('&'))
    def test_is_company_name_valid(self):
        """Does it validate company name?"""
        self.assertEqual('hello+and++++bonjour',pattern_web_scraper_functions.slug('hELlo &    BONjOUR'))

#gen_name
    def test_is_full_name_output(self):
        """Does it output first_name, last_name and full_name from a list?"""
        self.assertEqual(('josh','balla-muir','josh balla-muir'),pattern_web_scraper_functions.gen_name(['josh','balla-muir','hello','fvfvrvfrd']))
    def test_last_tooshort(self):
        """Does it identify when word is too short?"""
        self.assertEqual('Not found',pattern_web_scraper_functions.gen_name(['balla-muir']))
    def test_blacklist(self):
        """Does it identify when a blacklisted word appears?"""
        self.assertEqual('Not found',pattern_web_scraper_functions.gen_name(['josh','profiles']))
#linkedin_google_search
    def test_is_synonyms_1_selected(self):
        """Does it select the correct list?"""
        self.assertEqual([
            'https://www.google.co.uk/search?q=testchief executive officer+linkedin',
            'https://www.google.co.uk/search?q=testceo+linkedin',
            'https://www.google.co.uk/search?q=testdirector+linkedin',
            'https://www.google.co.uk/search?q=testhead of company+linkedin',
            'https://www.google.co.uk/search?q=testchairman+linkedin',
            'https://www.google.co.uk/search?q=testfounder+linkedin'
                ],pattern_web_scraper_functions.linkedin_google_search('ceo'))
    def test_is_synonyms_2_selected(self):
        """Does it select the correct list?"""
        self.assertEqual([
            'https://www.google.co.uk/search?q=testchief financial officer+linkedin',
            'https://www.google.co.uk/search?q=testcfo+linkedin',
            'https://www.google.co.uk/search?q=testhead of finance+linkedin',
            'https://www.google.co.uk/search?q=testaccounts+linkedin',
            'https://www.google.co.uk/search?q=testhead of accounts+linkedin',
            'https://www.google.co.uk/search?q=testtreasurer+linkedin'
                ],pattern_web_scraper_functions.linkedin_google_search('cfo'))
    def test_is_synonyms_3_selected(self):
         """Does it select the correct list?"""
         self.assertEqual([
            'https://www.google.co.uk/search?q=testchief technology officer+linkedin',
            'https://www.google.co.uk/search?q=testcto+linkedin',
            'https://www.google.co.uk/search?q=testtechnology director+linkedin',
            'https://www.google.co.uk/search?q=testhead of technology+linkedin',
            'https://www.google.co.uk/search?q=testdevelopment+linkedin',
            'https://www.google.co.uk/search?q=testchief of technology+linkedin'
                 ],pattern_web_scraper_functions.linkedin_google_search('cto'))
    def test_is_synonyms_1_selected_alternate(self):
        """Does it select the correct list?"""
        self.assertEqual([
            'https://www.google.co.uk/search?q=testchief executive officer+linkedin',
            'https://www.google.co.uk/search?q=testceo+linkedin',
            'https://www.google.co.uk/search?q=testdirector+linkedin',
            'https://www.google.co.uk/search?q=testhead of company+linkedin',
            'https://www.google.co.uk/search?q=testchairman+linkedin',
            'https://www.google.co.uk/search?q=testfounder+linkedin'
                ],pattern_web_scraper_functions.linkedin_google_search('chairman'))
    def test_is_synonyms_2_selected_alternate(self):
        """Does it select the correct list?"""
        self.assertEqual([
            'https://www.google.co.uk/search?q=testchief financial officer+linkedin',
            'https://www.google.co.uk/search?q=testcfo+linkedin',
            'https://www.google.co.uk/search?q=testhead of finance+linkedin',
            'https://www.google.co.uk/search?q=testaccounts+linkedin',
            'https://www.google.co.uk/search?q=testhead of accounts+linkedin',
            'https://www.google.co.uk/search?q=testtreasurer+linkedin'
                ],pattern_web_scraper_functions.linkedin_google_search('treasurer'))
    #def test_is_synonyms_3_selected_alternate(self):
    #     """Does it select the correct list?"""
    #     self.assertEqual([
    #        'https://www.google.co.uk/search?q=testchief technology officer+linkedin',
    #        'https://www.google.co.uk/search?q=testcto+linkedin',
    #        'https://www.google.co.uk/search?q=testtechnology director+linkedin',
    #        'https://www.google.co.uk/search?q=testhead of technology+linkedin',
    #        'https://www.google.co.uk/search?q=testdevelopment+linkedin',
    #        'https://www.google.co.uk/search?q=testchief of technology+linkedin'
    #             ],pattern_web_scraper_functions.linkedin_google_search('technology director
    #             '))

#html_dump_prep
#word_finder
#name_compilation
#name_final
#gen_html_text

if __name__ == '__main__':
    unittest.main()
#add != as well as =
