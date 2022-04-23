import os
import json
from config_4 import config  #python file contains 4 accounts
from twarc import Twarc  #need install
import datetime
from multiprocessing import Process
import couchdb #need install
from couchdb_address import host, port, username, password, db_name #python file connected with couchdb info



#this function is for connecting with database in couchdb
# if the database we want does not exist, just create it
def connect_with_db(db_name, server):
    try:
        return server[db_name]
    except:
        return server.create(db_name)



#this function is for connecting with couchdb server
#the attributes are listed in crawlerSetting file
def connect_with_couchdb(username, password, host, port):
    cdb_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return cdb_server


server = connect_with_couchdb(username, password, host, port)
db = connect_with_db(db_name, server)



#this function is to send the twitter we clawed to the database
def twitter_to_couchDB(t, db=db):
#make sure no same tweet
    if str(t["id"]) not in db:

        t["_id"] = "%d" % t["id"]
#make sure the contents are all in "text" key
        if "full_text" in t:
            t["text"] = t["full_text"]
            del t["full_text"]
#make sure the text can show all for great analysis
        if t["truncated"]:
            t["text"] = t["extended_tweet"]["full_text"]

        tweet={}
        tweet["id"] = int(t["_id"])
        if "text" in t:
            tweet["text"] = t["text"]
        if "user" in t:
            tweet["user"] = t["user"]
        if "lang" in t:
            tweet["lang"] = t["lang"]
        if "created_at" in t:
            tweet["created_at"] = t["created_at"]
        if "geo" in t:
            tweet["geo"] = t["geo"]
        if "place" in t:
            tweet["place"] = t["place"]

        if tweet is not None:
            try:
                db.save(tweet)
            except:
                pass



#this is the process to claw tweet
def claw_twitter(acc, city_boundding):

     four_city = {"Sydney": [149.971885992, -34.33117400499998, 151.63054702400007, -32.99606922499993],
             "Melbourne": [144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995],
             "Brisbane": [152.07339276400012, -28.363962911999977, 153.54670756200005, -26.452339004999942],
             "Adelaide": [138.435645001, -35.350296029999974, 139.04403010400003, -34.50022530299998]}

#using Twarc to get tw
     tw = Twarc(**acc['account'])
#format for location
     lo = ",".join([str(i) for i in four_city[city_boundding]])

     for tweet in tw.filter(locations=lo):
        twitter_to_couchDB(tweet)
        print("1")








if __name__ == "__main__":

    accounts = config.tokens
    cities = ["Sydney", "Melbourne", "Brisbane", "Adelaide"]
    all_things = []

    for i in range(len(accounts)):

        multi_pro = Process(target=claw_twitter, args=(accounts[i], cities[i]), daemon=True)
        all_things.append(multi_pro)
        multi_pro.start()
    [p.join() for p in all_things]
