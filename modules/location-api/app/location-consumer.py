import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from kafka import KafkaConsumer
import logging

"""
Sample implementation of a writer that can be used to read messages from gRPC.
"""

# Update this with desired payload
# convert datetime to timestamp to comform to grpc proto definition

def ConsumeLocation():
    TOPIC_NAME = 'locations'
    consumer = KafkaConsumer(TOPIC_NAME)
    for message in consumer:
        logging.info("message ...", message)

if __name__ == "__main__":
    ConsumeLocation()
