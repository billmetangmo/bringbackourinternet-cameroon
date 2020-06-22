
import os
import json
from collections import Counter

def read_lines_as_json(path):

        if os.path.exists(path):
            # warning if remote filesystem this means nothing but we assume there a local posix filesystem
            data = []
            if os.access(path, os.R_OK):
                with open(path, 'r') as fd:
                    for line in fd:
                        data.append(json.loads(line))
                return data
            else:
                raise ValueError("Bad rights when trying to read data from file"+path+".")
                


if __name__ == "__main__":
    
    # 5900 tweets du 18 au 29 avril
    tweets = read_lines_as_json("/home/ubuntu/environment/tweets-bringbackourinternet.json")
    quotes,replies,retweets,favorites = 0,0,0,0
    for tweet in tweets:
        quotes = quotes + int(tweet.get("quote_count"))
        replies = replies + int(tweet.get("reply_count"))
        retweets = retweets + int(tweet.get("retweet_count"))
        favorites = favorites + int(tweet.get("favorite_count"))
        
    print("quotes = "+str(quotes))
    print("replies = "+str(replies))
    print("retweets = "+str(retweets))
    print("favorites = "+str(favorites))