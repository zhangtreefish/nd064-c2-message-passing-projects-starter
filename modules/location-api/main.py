import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(request_value)
        timestamp_dt = datetime.datetime.fromtimestamp(request.creation_time.seconds + request.creation_time.nanos / 1e9)
        timestamp_st=timestamp_dt.strftime("%m/%d/%Y, %H:%M:%S.%f")

        location_res = location_pb2.LocationMessageResponse(
            id=request.id,
            person_id=request.person_id,
            coordinate="010100000097FDBAD39D925EC0D00A0C59DDC64240",
            creation_time=timestamp_st
        )
        print(location_res)

        # return location_pb2.LocationMessageResponse(**location_res)
        return location_res

    def Retrieve(self, request, context):
        timestamp_dt = datetime.fromtimestamp(request.creation_time.seconds + request.creation_time.nanos / 1e9)
        timestamp_st=timestamp_dt.strftime("%m/%d/%Y, %H:%M:%S")

        location_res = location_pb2.LocationMessageResponse(
            id=request.id,
            person_id=request.person_id,
            coordinate="010100000097FDBAD39D925EC0D00A0C59DDC64240",
            creation_time=timestamp_st
        )
        result = location_pb2.Retrieve()
        print("giving you back some mock data for illustration purpose...")
        
        print(location_res)
        print(result)
        return location_res

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5006...")
server.add_insecure_port("[::]:5006")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
