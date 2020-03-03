"""
SoftDes Spring 2020
Mini Prject 3: Text Mining

@author: Sam Coleman
"""


import twitter
from config import consumer_key, consumer_secret, access_token, access_token_secret

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)
statuses = api.GetUserTimeline(25073877)
print(statuses)
