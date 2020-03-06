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
    Get tweets for user and save into a pickled file. The list is of all lowercase words (exlcuding hyperlinks)

    screen_name: twitter user's handle
    file_name: name of file to save tweets to
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

    #Save list of words to pickled file
    f = open(file_name, 'wb')
    pickle.dump(user_words, f)
    f.close()

def get_user_tweets(screen_name, file_name):
    """
    Get tweets for the user if file doesn't exist, if it does unpickle it

    screen_name: user's twitter handle
    file_name: Name of pickled file
    """
    file = Path(file_name)
    if file.is_file():
        input_file=open(file_name, 'rb')
        reloaded_words = pickle.load(input_file)
        return reloaded_words
    else:
        pull_tweets(screen_name, file_name)

def pull_all_tweets():
    """
    Pull tweets for Trump, Bernie, Biden
    """
    TrumpWords = get_user_tweets('@realdonaldtrump', 'TrumpTweets.pickle')
    BernieWords = get_user_tweets('@BernieSanders', 'BernieTweets.pickle')
    BidenWords = get_user_tweets('@JoeBiden', 'BidenTweets.pickle')
    return TrumpWords, BernieWords, BidenWords

if __name__ == '__main__':
    TrumpWords = get_user_tweets('@realDonaldTrump', 'TrumpTweets.pickle')
    BernieWords = get_user_tweets('@BernieSanders', 'BernieTweets.pickle')
    BidenWords = get_user_tweets('@JoeBiden', 'BidenTweets.pickle')
