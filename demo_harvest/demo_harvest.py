import couchdb #need install
from db_add import host, port, username, password, db_name #python file connected with couchdb info


#this function is for connecting with database in couchdb
# if the database we want does not exist, just create it
def connect_with_db(db_name, server):
    try:
        return server[db_name]
    except:
        return server.create(db_name)



def connect_with_couchdb(username, password, host, port):
    cdb_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return cdb_server


server = connect_with_couchdb(username, password, host, port)
db = connect_with_db(db_name, server)


def twitter_to_couchDB(t, db=db):
        tweet={}
        tweet["id"] = int(t["id"])

        if "text" in t:
            tweet["text"] = t["text"]

        if tweet is not None:
            try:
                db.save(tweet)
            except:
                pass



