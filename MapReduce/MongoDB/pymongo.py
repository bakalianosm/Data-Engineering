import pymongo
import os
import json
# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/twitter")

db = client["twitter"]
collection = db["tweets"]

# Define the folder 
input_folder = '/home/ubuntu/task_2_1'


for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'r') as file:
        #with open("./single_retweeted_sample.json", 'r') as file:
            for line in file.readlines():
                if line.strip(): 
                    data = json.loads(line)
                    collection.insert_one(data)

