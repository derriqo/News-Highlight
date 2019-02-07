import unittest
from app.models import source
# Source = source.Source


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('the-times-of-india','The Times of India',"Freed Saudis resurface billions poorer after crown prince's crackdown - Times of India", 'Middle East News: Almost 15 months after rounding up dozens of Saudi Arabia’s richest and most powerful people and imprisoning them in Riyadh’s Ritz-Carlton, crown prin.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))