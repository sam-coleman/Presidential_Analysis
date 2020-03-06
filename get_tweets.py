"""
SoftDes Spring 2020
Mini Prject 3: Text Mining

@author: Sam Coleman
"""

import tweepy, string, pickle
from config import consumer_key, consumer_secret, access_token, access_token_secret
from pathlib import Path

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = []

def pull_tweets(screen_name, file_name):
    """
    Get tweets for user and save into a txt file
    """
    user_tweets = []
    user_lines = []
    user_words = []
    for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode="extended", include_rts= 0).items():
        user_tweets.append(status.full_text)

    for line in user_tweets:
        processed_line = line.strip()
        processed = processed_line.lower().split()
        user_lines.append(processed)

    user_words = []
    for tweet in user_lines:
        for word in tweet:
            if not (word[0:4] == "http"):
                user_words.append(word.strip(string.punctuation))

    #Save to file
    f = open(file_name, 'wb')
    pickle.dump(user_words, f)
    f.close()

def get_user_tweets(screen_name, file_name):
    """
    Get tweets for the user if file doesn't exist, if it does unpickle it
    """
    file = Path(file_name)
    if file.is_file():
        input_file=open(file_name, 'rb')
        reloaded_words = pickle.load(input_file)
        return reloaded_words
    else:
        pull_tweets(screen_name, file_name)
        #get_user_tweets(screen_name, file_name)

TrumpWords = get_user_tweets('@realDonaldTrump', 'TrumpTweets.pickle')
BernieWords = get_user_tweets('@BernieSanders', 'BernieTweets.pickle')
BidenWords = get_user_tweets('@JoeBiden', 'BidenTweets.pickle')

# def get_trump_tweets():
#     """
#     Get Trump's Tweets if file doesn't exist, if it does unpickle it
#     """
#     file = Path('TrumpTweets.pickle')
#     if file.is_file():
#         input_file = open('TrumpTweets.pickle', 'rb')
#         reloaded_words = pickle.load(input_file)
#         return reloaded_words
#     else:
#         pull_tweets('@realDonaldTrump', 'TrumpTweets.pickle')
#
# def get_bernie_tweets():
#     """
#     Get Bernie's Tweets if file doesn't exist, if it does unpickle it
#     """
#     file = Path('BernieTweets.pickle')
#     if file.is_file():
#         input_file = open('BernieTweets.pickle', 'rb')
#         reloaded_words = pickle.load(input_file)
#         return reloaded_words
#     else:
#         get_tweets('@BernieSanders', 'BernieTweets.pickle')
#
# def get_biden_tweets():
#     """
#     Get Biden's Tweets if file doesn't exist, if it does unpickle it
#     """
#     file = Path('BidenTweets.pickle')
#     if file.is_file():
#         input_file = open('BidenTweets.pickle', 'rb')
#         reloaded_words = pickle.load(input_file)
#         return reloaded_words
#     else:
#         get_tweets('@JoeBiden', 'BidenTweets.pickle')

# BernieWords = get_bernie_tweets()
# TrumpWords = get_trump_tweets()
# BidenWords = get_biden_tweets()
