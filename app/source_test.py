import unittest
from app.models import source
Source = source.Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('the-times-of-india','The Times of India',"Freed Saudis resurface billions poorer after crown prince's crackdown - Times of India", 'Middle East News: Almost 15 months after rounding up dozens of Saudi Arabia’s richest and most powerful people and imprisoning them in Riyadh’s Ritz-Carlton, crown prin.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()