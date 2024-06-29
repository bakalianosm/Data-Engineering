import pymongo
import os
import json
import re
# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/twitter_replica")

db = client["twitter_replica"]
collection = db["tweets"]

words_to_count = ['han', 'hon', 'den', 'det', 'denna', 'denne', 'hen']
toAdd = False
id_map = {}
seen_ids = set()
for document in collection.find():
    word_counts_per_id =  {word: 0 for word in words_to_count}

    
    if ( (document.get("retweeted_status") != None) and (document["retweeted_status"]["id_str"]) != None):
        #print(f'Found that retweeted status exists in {document.get("retweeted_status")}')
        #print(f'id_str apo retweeted status = {document["retweeted_status"]["id_str"]}')
        if document["retweeted_status"]["id_str"] in seen_ids:
            continue
        else:
            toAdd = True

    else:
        toAdd = True
    

    if toAdd:
        seen_ids.add(document["id_str"])
        words = document["text"].split()

    for word in words:
        if word.lower() in words_to_count:
            word_counts_per_id[word.lower()] += 1

    id_map[document["id_str"]] = word_counts_per_id    

for id, count_map in id_map.items():
    for word, count in count_map.items():
        print(f'{word}\t{count}') 



       