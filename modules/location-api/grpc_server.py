import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
import location.location_service


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("before timestamp_dt")
        timestamp_dt = datetime.fromtimestamp(request.creation_time.seconds + request.creation_time.nanos / 1e9)
        # location_dt = datetime.fromtimestamp(request.creation_time)
        print("after timestamp_dt= ", timestamp_dt)  # 2021-11-07 14:30:53.096698

        timestamp_st=timestamp_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        print("after timestamp_st= ", timestamp_st)  # 


        # construct the dict object needed for calling svc:
        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": str(request.longitude),
            "latitude": str(request.latitude),
            "creation_time": timestamp_st
        }
        print("request_value=", request_value)
     
     

        """ location_res = location_pb2.LocationMessageResponse(
            id=request.id,
            person_id=request.person_id,
            coordinate="010100000097FDBAD39D925EC0D00A0C59DDC64240",
            creation_time=timestamp_st
        )
        print("location_res")
        print(location_res) """

        # return location_pb2.LocationMessageResponse(**location_res)
        # return location_res
        # result_from_svc = app.location_service.LocationService.Create(location_pb2.LocationMessageResponse(**location_res))
        result_from_svc = app.location_service.LocationService.Create(request_value)
        return result_from_svc

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

# call create_app() in the grpc server:
import os

from location import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(debug=True)
# end

print("Server starting on port 5006...")
server.add_insecure_port("[::]:5006")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
