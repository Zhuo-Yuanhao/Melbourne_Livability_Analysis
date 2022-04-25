import couchdb
import json
from connect_to_DB import *

def trail1():
    database = connect_to_database()
    dic={}
    i=0

    for item in database:
        row=database[item]
        #print(row['text'])#这里改名字就读列；用row.keys()可以返回所有key(不是个list，只能手动填代码里)
        if row['place']:
            place = row['place']['name']
            if row['lang']=='en' or row['lang']=='en-gb':
                if place in dic:
                    en=dic[place][0]
                    nonen=dic[place][1]
                    dic[place]=[en+1,nonen,nonen/(en+1+nonen)]
                else:
                    dic[place]=[1,0,0]
            else:
                if place in dic:
                    en=dic[place][0]
                    nonen=dic[place][1]
                    dic[place]=[en,nonen+1,nonen/(en+1+nonen)]
                else:
                    dic[place]=[0,1,1]
        i=i+1
        if i%1000==0:
            print(i)
        if i>300000:
            break
    #outFileName = 'data/language.json'
    #with open(outFileName,'w') as f:
        #json.dump(dic,f)
    return json.dump(dic)
