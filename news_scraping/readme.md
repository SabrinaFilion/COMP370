The News Scraping folder consists of an assignment done for the COMP370 class at McGill.
Collector parses the arguments given: the api key, the input file, the output file and the lookback days.
It then calls the function fetch_latest_news from newsapi.py on every keyword provided in the input file.
fetch_latest-news requests NewsAPI for the articles corresponding to the keywords and lookback days.
It writes the output of the function in the output file.

This is how it would be used in the command line:
python collector.py -k apikey -i kamala_cat.json -o data_kamala_10