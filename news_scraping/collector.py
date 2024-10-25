from argparse import ArgumentParser
import json
from .newsapi import fetch_latest_news


def collector(api_key,lookback,input_file,output_file):
    with open(input_file, 'r') as file:
        input= json.load(file)
    #for each keyword set query the keywords and write results to output
    for name,keyword_set in input.items():
        articles=fetch_latest_news(api_key=api_key,news_keywords=keyword_set,lookback_days=lookback)
        with open(output_file, 'w') as json_file:
            json.dump(articles, json_file, indent=4)


def main():
    parser = ArgumentParser()
    parser.add_argument('-k','--api_key',help='api key')
    parser.add_argument('-b','--lookback',type=int,help='The number of lookback days')
    parser.add_argument('-i','--input',help='The input file in json format')
    parser.add_argument('-o','--output',help='The output file')
    args=parser.parse_args()
    
    collector(args.api_key,args.lookback,args.input,args.output)

if __name__ == '__main__':
   main()