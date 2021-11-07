import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a getter-or reader from gRPC.
"""

print("Reading orders...")

channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
stub = order_pb2_grpc.OrderServiceStub(channel)

#Getter

response = stub.Get(order_pb2.Empty())
print("Orders read include: ...")
print(response)