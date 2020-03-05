import twitter, pickle
from config import consumer_key, consumer_secret, access_token, access_token_secret


#api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)


trump = []
bernie = []
biden = []
warren = []


def load():
    """
    trump_input = open('trumpTweets.txt', 'rb')
    load.trump = pickle.load(trump_input)

    bernie_input = open('bernieTweets.txt', 'rb')
    load.bernie = pickle.load(bernie_input)

    biden_input = open('bidenTweets.txt', 'rb')
    load.biden = pickle.load(biden_input)

    warren_input = open('warrenTweets.txt', 'rb')
    load.warren = pickle.load(warren_input)

    return load.trump, load.biden, load.bernie, load.warren
    """
    global trump
    trump_input = open('trumpTweets.txt', 'rb')
    trump = pickle.load(trump_input)

    global bernie
    bernie_input = open('bernieTweets.txt', 'rb')
    bernie = pickle.load(bernie_input)

    global biden
    biden_input = open('bidenTweets.txt', 'rb')
    biden = pickle.load(biden_input)

    global warren
    warren_input = open('warrenTweets.txt', 'rb')
    load.warren = pickle.load(warren_input)

    return trump


load()
#print(load.warren)

# warren = load.warren
# trump = load.trump
# bernie = load.bernie
# biden = load.biden
# #print(trump)
# testFile = open('TrumpTweetsDelete', 'w')
# testFile.write(str(trump))
# testFile.close()

print(trump.text)
#print(trump['text'])
