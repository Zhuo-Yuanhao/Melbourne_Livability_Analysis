import tweepy
from demo_harvest import *


bearer_token = "###############"

client = tweepy.Client(bearer_token)

q = 'covid OR covid19 OR good OR terrible OR bad'


for tweet in tweepy.Paginator(client.search_recent_tweets, query=q, max_results=100).flatten(limit=20000):
    twitter_to_couchDB(tweet)
