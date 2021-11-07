import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
timestamp = Timestamp()
now = datetime.datetime.now()
timestamp.FromDatetime(now)
location_req = location_pb2.LocationMessageRequest(
            id="2222",
            person_id=555,
            longitude=-71.104,
            latitude=42.315,
            creation_time=timestamp
        )

response = stub.Create(location_req)
