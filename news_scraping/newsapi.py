import requests
from datetime import datetime,timedelta
URL="https://newsapi.org/v2/everything"

#Function that queries the NewsAPI, returning a list of news articles in English,
# containing the keywords given, and published in the last lookback days
def fetch_latest_news(api_key, news_keywords, lookback_days):
    
    #Checking if the news keywords are present
    if(not news_keywords):
        raise ValueError("Please provide keywords")
    #checking keywords only contain alphabetical characters
    for keyword in news_keywords:
        if( not keyword.isalpha()):
            raise ValueError("Keywords must contain only alphabetical characters")
    
    #Getting the requests with all the appropriate parameters
    response = requests.get(URL,params={"q":news_keywords,
                                        "language":"en",
                                        "from":(datetime.now()-timedelta(days=lookback_days)),
                                        "apiKey":api_key})
    data= response.json()
    return data

