import pulsar

INPUT_STRING = "I want to be capatilized"


client = pulsar.Client('pulsar://localhost:6650')  
producer = client.create_producer("assignment1-topic")

for word in INPUT_STRING.split(" "):
    producer.send(word.encode("utf-8"))
producer.close()
client.close()