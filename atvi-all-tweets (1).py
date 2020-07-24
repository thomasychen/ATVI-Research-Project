# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:31:55 2020

@author: kid3
"""

api_key = 'sSQ53ODOXFKwNPZ3hqipw5DAi'
api_secret = 'K2lpIyYaUk4qQ6MVMM8mu4pQsGhQVv9eIaWHXp8CfLeTJM8mgP'
access_token = '1281073480193044482-nEXTz7OsExPRILaaWYB5v4e4zvf9Xh' 
access_secret = '44i8KGgX20zF8y3HG4iju6ImWVFrWs4MZh7199PyM1H9H'

from TwitterAPI import TwitterAPI, TwitterPager
import json
import time

SEARCH_TERM = '$ATVI'
PRODUCT = 'fullarchive'
LABEL='datastrategyproject'

file = open('ATVI.json', 'w', encoding='utf-8')

api = TwitterAPI(api_key, 
                 api_secret,
                 access_token,
                 access_secret)

r = api.request('tweets/search/%s/:%s' % (PRODUCT, LABEL), 
            {'query':SEARCH_TERM, 
            'fromDate':'201901010000',
            'toDate':'202007082220'
            }
            )
print(r, r.status_code)
next = ''
while r.status_code == 200:
    r_json = r.json()
    print("dumping...")
    json.dump(r_json, file, ensure_ascii=False, indent=4)
    if 'next' not in r_json:
        break
    else:
        next = r_json['next']

    time.sleep(5)
    r = api.request('tweets/search/%s/:%s' % (PRODUCT, LABEL), 
                    {'query':SEARCH_TERM, 
                     'fromDate':'201901010000',
                     'toDate':'202007082220',
                     'next':next})


#pager = TwitterPager(api, 'tweets/search/fullarchive/:datastrategyproject',
#    {'q': SEARCH_TERM,'fromDate':201901010000,'toDate':202007082216})

#for item in pager.get_iterator():
#    print("dumping...")
#    json.dump(item, file, ensure_ascii=False, indent=4)

file.close()