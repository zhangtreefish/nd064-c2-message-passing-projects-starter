import grpc
import location_pb2
import location_pb2_grpc
import location_service

from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from kafka import KafkaConsumer
import logging
from google.protobuf.json_format import MessageToDict

"""
Sample implementation of a kafka consumer that can be used to read messages from gRPC.
"""

# Update this with desired payload
# convert datetime to timestamp to comform to grpc proto definition

def ConsumeLocation():
    TOPIC_NAME = 'locations'
    KAFKA_URL = 'kafka.default.svc.cluster.local'
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_URL)
    
    for message in consumer:
        logging.info("message before persisting into db ...", message)
        # send the location data to db:
        location_obj = MessageToDict(message)
        location_service.LocationService.Create(location_obj) 
        logging.info("after callling LocationService...")

if __name__ == "__main__":
    ConsumeLocation()
