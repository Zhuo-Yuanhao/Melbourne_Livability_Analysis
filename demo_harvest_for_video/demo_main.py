import tweepy
from demo_harvest import *


bearer_token = "AAAAAAAAAAAAAAAAAAAAAD1xbgEAAAAASXrPTL92IrSR%2FppXimNnPN5elyA%3DnT5A1poO57o16wYI1uWUlSoG4CAPBjDNvBuQahPP2tKYN1AB12"

client = tweepy.Client(bearer_token)

q = 'covid OR covid19 OR good OR terrible OR bad'


for tweet in tweepy.Paginator(client.search_recent_tweets, query=q, max_results=100).flatten(limit=20000):
    twitter_to_couchDB(tweet)