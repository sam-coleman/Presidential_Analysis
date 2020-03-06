"""
SoftDes Spring 2020
Mini Prject 3: Text Mining

@author: Sam Coleman
"""


import twitter, pickle, string
from config import consumer_key, consumer_secret, access_token, access_token_secret

def get_tweets():

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    #Trumps tweets
    trump_tweets = api.GetUserTimeline(25073877, include_rts= 0, count = 199, tweet_mode='extended') #Trump's Tweets
    trump_tweets1 = []
    lines_trump = []
    for i in trump_tweets: #create list of text of Tweets
        trump_tweets1.append(i.fulltext)
        print(trump_tweets1)

    for line in trump_tweets1:
        processed_line = line.strip()
        processed = processed_line.lower().split()
        lines_trump.append(processed)

    words_trump= [] #Final list we want and care about
    for tweet in lines_trump:
        for word in tweet:
                #print(word[0:4])
            if not (word[0:4] == "http"):
                words_trump.append(word.strip(string.punctuation))

    trump = open('TrumpTweets.txt', 'w')
    trump.write(str(words_trump))
    trump.close()

    #For Bernie
    bernie_tweets = api.GetUserTimeline(216776631, include_rts= 0, count = 199) #Bernie's Tweets
    bernie_tweets1 = []
    lines_bernie = []
    for i in bernie_tweets: #create list of text of Tweets
        bernie_tweets1.append(i.text)
        #print(trump_tweets1)

    for line in bernie_tweets1:
        processed_line = line.strip()
        processed = processed_line.lower().split()
        lines_bernie.append(processed)

    words_bernie= [] #Final list we want and care about
    for tweet in lines_bernie:
        for word in tweet:
                #print(word[0:4])
            if not (word[0:4] == "http"):
                words_bernie.append(word.strip(string.punctuation))

    bernie = open('BernieTweets.txt', 'w')
    bernie.write(str(words_bernie))
    bernie.close()

    #For Biden
    biden_tweets = api.GetUserTimeline(939091, include_rts= 0, count = 199) #Biden's Tweets
    biden_tweets1 = []
    lines_biden = []
    for i in biden_tweets: #create list of text of Tweets
        biden_tweets1.append(i.text)
        #print(trump_tweets1)

    for line in biden_tweets1:
        processed_line = line.strip()
        processed = processed_line.lower().split()
        lines_biden.append(processed)

    words_biden= [] #Final list we want and care about
    for tweet in lines_biden:
        for word in tweet:
                #print(word[0:4])
            if not (word[0:4] == "http"):
                words_biden.append(word.strip(string.punctuation))

    biden = open('BidenTweets.txt', 'w')
    biden.write(str(words_biden))
    biden.close()

    #For Warren
    warren_tweets = api.GetUserTimeline(357606935, include_rts= 0, count = 199) #Warren's Tweets
    warren_tweets1 = []
    lines_warren = []
    for i in warren_tweets: #create list of text of Tweets
        warren_tweets1.append(i.text)
        #print(trump_tweets1)

    for line in warren_tweets1:
        processed_line = line.strip()
        processed = processed_line.lower().split()
        lines_warren.append(processed)

    words_warren = [] #Final list we want and care about
    for tweet in lines_warren:
        for word in tweet:
                #print(word[0:4])
            if not (word[0:4] == "http"):
                words_warren.append(word.strip(string.punctuation))

    warren = open('WarrenTweets.txt', 'w')
    warren.write(str(words_warren))
    warren.close()

    return words_biden, words_trump, words_bernie, words_warren
get_tweets()
