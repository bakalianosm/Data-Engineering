import time 
from pulsar import Client, ConsumerType


def conversion(substring, operation):
    """A conversion function which takes a string as an input and outputs a converted string

    Args:
        substring (String)
        operation (function): This is an operation on the given input

    Returns:
        [String]: Converted String
    """
    # returns the conversion applied to input
    return operation(substring)

def function(string):
    """A function that performs some operation on a string. You can change the operation accordingly

    Args:
        string (String): input string on which some operation is applied

    Returns:
        [String]: string in upper case
    """
    return string.upper()


service_url = "pulsar://localhost:6650"
ITERATION = 5


def consumer():
    
    # Establish connection to the Pulsar client
    client = Client('pulsar://localhost:6650')

    # Subscribe to the topic with the specified subscription name
    consumer = client.subscribe(topic= "assignment1-topic", subscription_name="assignment1-subcription")
    
    for i in range(0, ITERATION):
        msg = consumer.receive()
        try:
            print("Received word '{}' id='{}'".format(msg.data().decode("utf-8"), msg.message_id()))
            # decode the received message because it is not in utf-8
            word = msg.data().decode("utf-8")
            print("Resultant String: {}".format(conversion(word, function)))
            consumer.acknowledge(msg)

        except Exception:
            print("There was a problem. Try running the application again")
            consumer.negative_acknowledge(msg)

    consumer.close()
    

if __name__ == "__main__":
    consumer()
