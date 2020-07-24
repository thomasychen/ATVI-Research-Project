# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:43:24 2020

@author: kid3
"""


from textblob import TextBlob
#use an existing model
from textblob.sentiments import NaiveBayesAnalyzer

#blob = TextBlob("I'm not convinced that $ATVI is managing this transition as adeptly.The companies monthly active user count has been falling", analyzer=NaiveBayesAnalyzer())
#print(blob.sentiment)

#train our own model
#from textblob.classifiers import NaiveBayesClassifier
#with open('$ATVI.csv', 'r', encoding = "utf-8") as fp:
#    cl = NaiveBayesClassifier(fp, format="csv")
#print(cl.classify("short the shits out of this stock"))

import json

#functions
def extractTime(created_at):
    clocktime= created_at.split(" ")
    year=clocktime[5]
    month= clocktime[1]
    day = clocktime[2]
    return (year+"-"+month+"-"+day)

#count negative comments daily
daily_neg = {}  
#count positive comments daily
daily_pos = {}

with open('ATVI30.json', 'r', encoding="utf-8") as json_file: 
    data = json_file.read()
    new_data = data.replace('}{', '},{')
    json_data = json.loads(f'[{new_data}]') 
    for one_json in json_data:
        results = one_json['results']
        for item in results:
            ts = extractTime(item['created_at'])
            tweet = item['text']
            text0 = tweet.replace(',',' ')
            text1 = text0.replace('\n','')
            text2 = text1.lower()
            if item["lang"]=="en" and text2.find('$atvi') >= 0:
                print(ts)
                print(text2)
                blob = TextBlob(text2, analyzer=NaiveBayesAnalyzer())
                print(blob.sentiment)
                if blob.sentiment.classification == 'pos':
                    if ts in daily_pos.keys():
                        daily_pos[ts] = daily_pos[ts] + 1
                    else:
                        daily_pos[ts] = 1
                else:
                    if ts in daily_neg.keys():
                        daily_neg[ts] = daily_neg[ts] + 1
                    else:
                        daily_neg[ts] = 1
                    
csv_file = open("daily_pos.csv", "w")
for ts in daily_pos.keys():
    csv_file.write(ts + ',' + str(daily_pos[ts]) + ',' + str(daily_neg[ts]) + '\n')

csv_file.close()