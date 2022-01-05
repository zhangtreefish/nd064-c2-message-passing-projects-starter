import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from kafka import KafkaProducer

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

# Update this with desired payload
# convert datetime to timestamp to comform to grpc proto definition

def ReceiveLocation():
    # below produces just a stub:
    timestamp = Timestamp()
    now = datetime.datetime.now()
    timestamp.FromDatetime(now)
    
    location = {
                person_id:5,
                longitude:-71.104,
                latitude:42.315,
                creation_time:timestamp
    }
    return location

def PublishLocation():
    TOPIC_NAME = 'locations'
    KAFKA_SERVER = 'kafka.default.svc.cluster.local' # 'localhost:9092'

    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    location_object = ReceiveLocation()
    message = str(location_object)
    producer.send(TOPIC_NAME, message)
    producer.flush()

if __name__ == "__main__":
    PublishLocation()
