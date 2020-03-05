"""
SoftDes Spring 2020
Mini Prject 3: Text Mining

@author: Sam Coleman
"""


import twitter, pickle
from config import consumer_key, consumer_secret, access_token, access_token_secret

def get_tweets():

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
    trump_tweets = api.GetUserTimeline(25073877, count = 200) #Trump's Tweets
    #print(trump_tweets)
    trump = open('trumpTweets.txt', 'wb')
    trump = pickle.dump(trump_tweets, trump)


    bernie_tweets = api.GetUserTimeline(216776631) #Bernie's Tweets
    bernie = open('bernieTweets.txt', 'wb')
    bernie = pickle.dump(bernie_tweets, bernie)

    biden_tweets = api.GetUserTimeline(939091) #Biden Tweets
    biden = open('bidenTweets.txt', 'wb')
    biden = pickle.dump(biden_tweets, biden)

    warren_tweets = api.GetUserTimeline(357606935) #Warren Tweets
    warren = open('warrenTweets.txt', 'wb')
    warren = pickle.dump(warren_tweets, warren)
    return trump, bernie, biden, warren
get_tweets()
