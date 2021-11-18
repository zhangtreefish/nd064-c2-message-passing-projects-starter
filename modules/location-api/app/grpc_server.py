import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
import location_service
from random import randint
import json


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("before timestamp_dt")
        timestamp_dt = datetime.fromtimestamp(request.creation_time.seconds + request.creation_time.nanos / 1e9)
        # print("after timestamp_dt= ", timestamp_dt)  # 2021-11-07 14:30:53.096698

        timestamp_st=timestamp_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        # print("after timestamp_st= ", timestamp_st)  # 

        # construct the dict object needed for calling svc:
        id = randint(100, 1000)

        request_value = {
            "person_id": request.person_id,
            "longitude": str(request.longitude),
            "latitude": str(request.latitude),
            "creation_time": timestamp_st
        }
        print("request_value=", request_value)

        location_res = location_pb2.LocationMessageResponse(
            id=53,
            person_id=request.person_id,
            coordinate="010100000097FDBAD39D925EC0D00A0C59DDC64240",
            creation_time=timestamp_st
        )

        result_from_db=location_service.LocationService.Create(request_value) 
        
        print("result_from_db= ", result_from_db)

        if result_from_db:
            return location_pb2.LocationMessageResponse(
                id=result_from_db.id,
                person_id=result_from_db.person_id,
                coordinate=str(result_from_db.coordinate),
                creation_time=cr_time)

        else:
            if location_res:
                return location_res
            else:
                context.set_code(grpc.StatusCode.UNKNOWN)
                context.set_details('New Location can not be created for some reason.')
                return location_pb2.Empty()

    def Retrieve(self, request, context):
        # set up a response stub in case db query does not work, so that I can validate grpc works:
        location_res = location_pb2.LocationMessageResponse(
            id=53,
            person_id=8,
            coordinate="010100000097FDBAD39D925EC0D00A0C59DDC64240",
            creation_time="2021-11-07 14:30:53.096698"
        )
        
        result_from_db = location_service.LocationService.Retrieve(request.id)         

        if result_from_db:
            return location_pb2.LocationMessageResponse(
                id=result_from_db.id,
                person_id=result_from_db.person_id,
                coordinate=str(result_from_db.coordinate),
                creation_time=result_from_db.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f')
                )
        else:
            # return the stub in the event of no result_from_db:
            if location_res:
                return location_res
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Location with id %s not found' % request.id)
                return location_pb2.Empty()

def serve():
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

if __name__ == "__main__":
    serve()
