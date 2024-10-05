import requests
from datetime import datetime,timedelta
URL="https://newsapi.org/v2/everything"

#Function which queries the NewsAPI, returning a list of news articles in english,
# containing the keyworfs and published in the last lookback days
def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    #Getting the requests with all appropriate parameters
    response = requests.get(URL,params={"q":news_keywords,
                                        "language":"en",
                                        "from":(datetime.now()-timedelta(days=lookback_days))})






if __name__ =="__main__":
    fetch_latest_news(5fb62789f7bd4435b2ae79c344b009c8,)