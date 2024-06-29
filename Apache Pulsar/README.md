
# Apache Pulsar


A simple `Apache Pulsar` project that demonstrates a basic setup of message production and consumption using Apache Pulsar, where messages are produced by `producer.py` script and consumed and processed by `consumer.py` script. In detail:

`producer.py` : Sends each word from a user defined input as separate messages to a Pulsar topic


`consumer.py` : Subscribes to the Pulsar topic, receives each message, applies the conversion, and prints them along with their message IDs. It then acknowledges each message.