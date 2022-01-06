import grpc
import location_pb2
import location_pb2_grpc

from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from kafka import KafkaConsumer
import logging
from google.protobuf.json_format import MessageToDict

"""
Sample implementation of a kafka consumer that can be used to write messages to gRPC server.
"""

# Update this with desired payload
# convert datetime to timestamp to comform to grpc proto definition

def ConsumeLocation():
    TOPIC_NAME = 'locations'
    KAFKA_SERVER = 'kafka.default.svc.cluster.local'
    # KAFKA_SERVER = 'localhost:9092'
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
    
    channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
    stub = location_pb2_grpc.LocationServiceStub(channel)

    while True:
        try:
            for message in consumer:
                logging.info("message before persisting into db ...", message)
                # send the location data to db via gRpc server:
                location_obj = MessageToDict(message)
                stub.Create(location_obj) 
                logging.info("after callling LocationService...")
        except:
            print("Something wrong during processing locations messages...")
        finally:
            consumer.close()
        

if __name__ == "__main__":
    ConsumeLocation()
