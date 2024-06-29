#!/usr/bin/env python
"""mapper.py"""


import sys
import json


words_to_count = ['han', 'hon', 'den', 'det', 'denna', 'denne', 'hen']
seen_ids = set()
id_map = {}
for line in sys.stdin:
    
    word_counts_per_id = {word: 0 for word in words_to_count}
    line.strip()
    if  line == "\n":
        continue

    tweet = json.loads(line)
    toAdd = False

    if "retweeted_status" in tweet and "id_str" in tweet["retweeted_status"]:
        if tweet["retweeted_status"]["id_str"] in seen_ids:
            #print(f'This tweet is a retweet from : {tweet["retweeted_status"]["id_str"]}, continuing...')
            continue
        else:
            #print(f'Not in seen ids, Adding {tweet["retweeted_status"]["id_str"]}...')
            toAdd = True
    else:
        #print(f'This is an original tweet, adding to the set {tweet["id_str"]}')
        toAdd  = True

    if toAdd:
        seen_ids.add(tweet["id_str"])
        words = line.split()

    for word in words:
        if word.lower() in words_to_count:
            word_counts_per_id[word.lower()] += 1

    id_map[tweet["id_str"]] = word_counts_per_id

for id, count_map in id_map.items():
    for word, count in count_map.items():
        print(f'{word}\t{count}') 

