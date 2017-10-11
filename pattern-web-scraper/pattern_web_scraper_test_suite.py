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
#gen_html_text
#html_dump_prep
#word_finder
#name_compilation
#name_final

if __name__ == '__main__':
    unittest.main()
