import couchdb

def connect_to_couch_db_server(host="172.26.129.242", port="5984", username="admin", password="admin"):
    secure_remote_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return secure_remote_server


def connect_to_database(database_name= "old_twitter_data", server=connect_to_couch_db_server()):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

