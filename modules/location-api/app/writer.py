import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
# convert datetime to timestamp to comform to grpc proto definition
timestamp = Timestamp()
now = datetime.datetime.now()
timestamp.FromDatetime(now)
# print("timestamp=", timestamp)
location_req = location_pb2.LocationMessageRequest(
            person_id=5,
            longitude=-71.104,
            latitude=42.315,
            creation_time=timestamp
        )
print("location_req before callling stub.Create ...", location_req)

response = stub.Create(location_req)
print("response after callling stub.Create ...", response)

