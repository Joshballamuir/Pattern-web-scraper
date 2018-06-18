import unittest
import pattern_web_scraper_functions

#example_test_variables:
subject = "mcdonalds"
synonyms = "/Users/josh/josh_github/Pattern-web-scraper/Employee_position_lists/cfo.csv"
blacklist = subject+synonyms+"/Users/josh/josh_github/Pattern-web-scraper/Employee_position_lists/position_blacklist.csv"

name_list = ['josh','balla-muir','hello','fvfvrvfrd']

class pattern_web_scraper_functions_TestCase(unittest.TestCase):
    """Tests for `new_name_finder_functions.py`."""


#TESTED:
#slug:
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


#TESTING:
#gen_name:
    def test_is_full_name_output(self):
        """Does it output first_name, last_name and full_name from a list?"""
        self.assertEqual('josh balla-muir josh balla-muir',pattern_web_scraper_functions.gen_name(name_list))
    def test_last_tooshort(self):
        """Does it identify when word is too short?"""
        self.assertEqual('Not found',pattern_web_scraper_functions.gen_name(['balla-muir']))
    def test_blacklist(self):
        """Does it identify when a blacklisted word appears?"""
        self.assertEqual('Not found',pattern_web_scraper_functions.gen_name(['josh','profiles']))


#UNTESTED:
#linkedin_google_search:
#    def test_is_synonyms_1_selected(self):
        #"""Does it select the correct list?"""
        #self.assertEqual([
        #    'https://www.google.co.uk/search?q=testchief executive officer+linkedin',
        #    'https://www.google.co.uk/search?q=testceo+linkedin',
        #    'https://www.google.co.uk/search?q=testdirector+linkedin',
        #    'https://www.google.co.uk/search?q=testhead of company+linkedin',
        #    'https://www.google.co.uk/search?q=testchairman+linkedin',
        #    'https://www.google.co.uk/search?q=testfounder+linkedin'
        #        ],pattern_web_scraper_functions.linkedin_google_search('ceo'))

#    def test_is_synonyms_1_selected_alternate(self):
    #    """Does it select the correct list?"""
    #    self.assertEqual([
    #        'https://www.google.co.uk/search?q=testchief executive officer+linkedin',
    #        'https://www.google.co.uk/search?q=testceo+linkedin',
    #        'https://www.google.co.uk/search?q=testdirector+linkedin',
    #        'https://www.google.co.uk/search?q=testhead of company+linkedin',
    #        'https://www.google.co.uk/search?q=testchairman+linkedin',
    #        'https://www.google.co.uk/search?q=testfounder+linkedin'
    #            ],pattern_web_scraper_functions.linkedin_google_search('chairman'))

#html_dump_prep
#word_finder
#name_compilation
#name_final
#gen_html_text

if __name__ == '__main__':
    unittest.main()
#add != as well as =
