import unittest
import os 
import json
import sys

with open("test_secrets.json","r") as file:
    api_key= json.load(file)
    
module_path=os.path.join(os.path.dirname(__file__), "newscover")
sys.path.append(module_path)
from newscover.newsapi import fetch_latest_news


class NewsAPITestCase(unittest.TestCase):
    def test_fail_nokeywords(self):
        with self.assertRaises(TypeError):
            fetch_latest_news(api_key,[],10)
            

    #def test_lookbackdays_respected(self):
        
        
    def test_fail_nonalpha_keyword(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key,"money$",10)