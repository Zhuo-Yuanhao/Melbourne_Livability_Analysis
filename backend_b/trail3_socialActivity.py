import couchdb
import json
import re
from connect_to_DB import *

def trail3():
    database = connect_to_database()
    dic={}
    i=0

    for item in database:
        row=database[item]
        if row['place']:
            place = row['place']['name']
            text = row['text']
            num_at=len(re.findall(r'@',text))
            num_hash=len(re.findall(r'#',text))
            atList=re.findall(r'@[a-zA-Z0-9_.+-]]',text)
            hashList=re.findall(r'#[a-zA-Z0-9_.+-]]',text)
            totalLen=len(text)
            sum=0
            for element in atList:
                sum=sum+len(element)
            for element in hashList:
                sum=sum+len(element)
            meaningfulLen=totalLen-sum
            if place in dic:
                total=dic[place][2]*(dic[place][1]+dic[place][0])+meaningfulLen
                if num_at < 0.5 and num_hash < 0.5:
                    dic[place] = [dic[place][0], dic[place][1]+1, total/(dic[place][1]+1+dic[place][0]),dic[place][0]/(dic[place][1]+1+dic[place][0])]
                else:
                    dic[place] = [dic[place][0]+1, dic[place][1], total/(dic[place][1]+1+dic[place][0]),(dic[place][0]+1)/(dic[place][1]+1+dic[place][0])]
            else:
                if num_at<0.5 and num_hash<0.5:
                    dic[place] = [0,1,meaningfulLen,0]
                else:
                    dic[place] = [1,0,meaningfulLen,1]

            i = i + 1
            if i % 1000 == 0:
                print(i)
            if i > 300000:
                break

    #outFileName = 'data/socialActivityAndWordsCount.json'
    #with open(outFileName,'w') as f:
        #json.dump(dic,f)
    return json.dump(dic)