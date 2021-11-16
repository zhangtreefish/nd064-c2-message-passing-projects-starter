import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a getter-or reader from gRPC.
"""

print("Reading orders...")

channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
stub = location_pb2_grpc.LocationServiceStub(channel)

req = location_pb2.RetrieveMessageRequest(id=51)
response = stub.Retrieve(req)
print("Location retrieved: ...", response)