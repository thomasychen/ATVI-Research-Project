# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:31:55 2020

@author: kid3
"""

consumer_key = 'tS4y2r9250ZHi5DX9PDuhHBJr'
consumer_secret = 'xaMlnJRpHzEhw1ULQJ8xjJVpryPtMiIlvoEClaYEAYh9mMwW0E'
access_token = '1084656297822187521-tuC2n5aOIPPow8fLitFjCwy36Q3PEd'
access_token_secret = 'miY0K6Kqmp9zvji5bRdczhyblrE4QElPDp3j9d5DXrLw4'

from TwitterAPI import TwitterAPI, TwitterPager
import json
import time
import csv


PRODUCT = '30day'
LABEL='datastrategyresearch'

csvFile = open('30-ATVI.csv', 'w',encoding='UTF-8')
csvWriter = csv.writer(csvFile)

api = TwitterAPI(consumer_key, 
                 consumer_secret,
                 access_token,
                 access_token_secret)

r = api.request('tweets/search/%s/:%s' % (PRODUCT, LABEL), {'query':'ATVI '})
print(r.json(), r.status_code)
next = ''
while r.status_code == 200:
    r_json = r.json()
    print("dumping...")
    for item in r:
        if item["lang"]=="en":
            csvWriter.writerow([item['created_at'],
                    item['text'] if 'text' in item else item])
    if 'next' not in r_json:
        break
    else:
        next = r_json['next']

    time.sleep(5)
    r = api.request('tweets/search/%s/:%s' % (PRODUCT, LABEL),{'query':'ATVI ', 'next':next})


#pager = TwitterPager(api, 'tweets/search/fullarchive/:datastrategyproject',
#    {'q': SEARCH_TERM,'fromDate':201901010000,'toDate':202007082216})

#for item in pager.get_iterator():
#    print("dumping...")
#    json.dump(item, file, ensure_ascii=False, indent=4)

csvFile.close()