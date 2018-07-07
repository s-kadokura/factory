#!/user/bin/env python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import csv
import json
import sys, codecs

search_words = input(u"Keyword?: ")

C_KEY = '6VECmbkydQt0pVWAyZrp1FscR'
C_SECRET = 'XhwsQiZq4us8nNmHmt8zOBqmHdlEx93gSjOcZh2NXcIa1iFQnQ'
A_KEY = '956166505007169536-hQ3CtS9V9oM4RdPtZUvnuuuiLcwTGtM'
A_SECRET = 'VDvTzJqL9yK0gVPCzJKJX16FMBmMVt04NrphWEQsiylpm'

def Search_words():
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
            "q": search_words,
            "lang": "ja",
            "result_type": "recent",
            "count": "100"
            }
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)
    req = tw.get(url, params = params)
    tweets = json.loads(req.text)

    f = open("tweetSearchResult.csv" , "w", encoding='CP932', errors='ignore')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['datetime', 'id', 'name', 'text'])

    for tweet in tweets["statuses"]:
        time = (tweet["created_at"])
        id = (tweet["user"]["screen_name"])
        name = (tweet["user"]["name"])
        text = (tweet["text"])

        writer.writerow([time, id, name, text])

    f.close()

    return Search_words

Search_words()
