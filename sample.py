# -*- coding: utf-8 -*-
__author__ = 'Juan David Carrillo López'

from TwitterAPI import TwitterAPI

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)
r = api.request('search/tweets', {'q': 'rayados', 'count': '100', 'lang': 'es'})

cont = 0
for item in r.get_iterator():
    cont += 1
    print item
print cont