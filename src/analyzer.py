from pythonosc.udp_client import SimpleUDPClient
from transformers import pipeline

#Initialize Pipelines
sentiment_pipeline = pipeline(
    "sentiment-analysis", model='cardiffnlp/twitter-roberta-base-sentiment-latest'
)

#helper functions
def affect_detector(sentence):
    """Compute the sentiment score of a sentence."""
    sentiment = sentiment_pipeline(sentence)[0]
    return sentiment['label'], sentiment['score']

def send_osc_message(ip: str, port: int, address: str, value1: float, value2: float):
    """
    Sends two float values via OSC.

    Parameters:
        ip (str): The destination IP address.
        port (int): The destination OSC port.
        address (str): The OSC address pattern (e.g., "/mydata").
        value1 (float): The first float value.
        value2 (float): The second float value.
    """
    
    client = SimpleUDPClient(ip, port)  # Create an OSC client
    client.send_message(address, [value1, value2])  # Send two floats as a list
