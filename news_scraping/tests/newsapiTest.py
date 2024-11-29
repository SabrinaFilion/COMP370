import unittest
import os 
import json
from datetime import timedelta, datetime

from newsapi import fetch_latest_news

#Getting the api_key
file_path = os.path.join(os.path.dirname(__file__), "test_secrets.json")
with open(file_path,"r") as file:
    data = json.load(file)
    api_key = data['api_key']
   
class NewsAPITestCase(unittest.TestCase):
        
    #Getting the api_key
    file_path = os.path.join(os.path.dirname(__file__), "test_secrets.json")
    with open(file_path,"r") as file:
        data = json.load(file)
        api_key = data['api_key']
    
    #Testing that the function raises an exception if we do not provide keywords
    def test_fail_nokeywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key,[],lookback_days=10)
            

    #Testing that the function respects the lookback days
    def test_lookback_days_respected(self):
        data=fetch_latest_news(self.api_key,["health"],lookback_days=5)
        articles=data['articles']
        for article in articles :
            publish_date=article['publishedAt'][:10]
            self.assertGreaterEqual(publish_date,(datetime.now()-timedelta(days=5)).strftime("%Y-%m-%d"))
            

    #Testing that the function raises an exception if the keywords contain non-alphabetical characters    
    def test_fail_nonalpha_keyword(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key,"money$",lookback_days=10)
            
