import tweepy
from demo_harvest import *


bearer_token = "AAAAAAAAAAAAAAAAAAAAAD1xbgEAAAAASXrPTL92IrSR%2FppXimNnPN5elyA%3DnT5A1poO57o16wYI1uWUlSoG4CAPBjDNvBuQahPP2tKYN1AB12"

client = tweepy.Client(bearer_token)

query = 'covid OR covid19 OR good OR terrible OR bad'
response = client.search_recent_tweets(query=query, max_results=97)

for tweet in response.data:
        twitter_to_couchDB(tweet)

