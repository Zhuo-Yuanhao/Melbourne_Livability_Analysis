import couchdb
import json
from textblob import TextBlob
from connect_to_DB import *

def trail2():
    database = connect_to_database()
    dic={}

    i=0
    for item in database:
        row=database[item]
        if row['place'] and (row['lang']=='en' or row['lang']=='en-gb'):
            place = row['place']['name']
            text=row['text']
            textblob=TextBlob(text)
            emotion=json.loads(textblob.json)[0]['polarity']
            subject=json.loads(textblob.json)[0]['subjectivity']
            weightedEmotion=emotion*subject
            if weightedEmotion>0.1:
                if place in dic:
                    positive = dic[place][0]
                    neutral = dic[place][1]
                    negative = dic[place][2]
                    total=dic[place][3]*(positive+neutral+negative)
                    dic[place] = [positive+1,neutral,negative,(total+weightedEmotion)/(positive+1+neutral+negative)]
                else:
                    dic[place] = [1, 0, 0,weightedEmotion]
            elif weightedEmotion<-0.1:
                if place in dic:
                    positive = dic[place][0]
                    neutral = dic[place][1]
                    negative = dic[place][2]
                    total=dic[place][3]*(positive+neutral+negative)
                    dic[place] = [positive,neutral,negative+1,(total+weightedEmotion)/(positive+1+neutral+negative)]
                else:
                    dic[place] = [0,0,1,weightedEmotion]
            else:
                if place in dic:
                    positive = dic[place][0]
                    neutral = dic[place][1]
                    negative = dic[place][2]
                    total=dic[place][3]*(positive+neutral+negative)
                    dic[place] = [positive,neutral+1,negative,(total+weightedEmotion)/(positive+1+neutral+negative)]
                else:
                    dic[place] = [0,1,0,weightedEmotion]
            i = i + 1
            if i % 1000 == 0:
                print(i)
            if i > 300000:
                break

    outFileName = 'data/emotion.json'
    with open(outFileName,'w') as f:
        json.dump(dic,f)
