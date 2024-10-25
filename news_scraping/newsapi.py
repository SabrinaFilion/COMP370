import requests
from datetime import datetime,timedelta
URL="https://newsapi.org/v2/everything"

#Function that queries the NewsAPI, returning a list of news articles in english,
# containing the keywords given and published in the last lookback days
def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    #Checking if the news keywords are present
    if(not news_keywords):
        raise ValueError("Please provide keywords")
    #checking keywords only contain alphabetical characters
    for keyword in news_keywords:
        if( not keyword.isalpha()):
            raise ValueError("Keywords must contain only alphabetical characters")
    
    #Getting the requests with all appropriate parameters
    response = requests.get(URL,params={"q":news_keywords,
                                        "language":"en",
                                        "from":(datetime.now()-timedelta(days=lookback_days)),
                                        "apiKey":api_key})
    data= response.json()
    return data



if __name__ =="__main__":
    
    data=fetch_latest_news("5fb62789f7bd4435b2ae79c344b009c8",["money"],10)
    print(data)