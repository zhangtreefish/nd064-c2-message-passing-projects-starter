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

        result_from_db=location_service.LocationService.Create(request_value)  # AttributeError: to_dict with to_dict()
        # AttributeError: 'dict' object has no attribute 'to_dict'
        # "TypeError: Create() got an unexpected keyword argument 'id'" : without to_dict
        # stub_from_svc = location_service.LocationService.Create(request_value)
        print("result_from_db= ", result_from_db)

        if result_from_db:
            return location_pb2.LocationMessageResponse(**result_from_db.to_dict())
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
        # print("giving you back some mock data for illustration purpose...")
        # print("location_res: ", location_res)

        result_from_db = location_service.LocationService.Retrieve(request.id) # 
        print("result_from_db.id ", result_from_db.id)                 # 66
        print("result_from_db.person_id ", result_from_db.person_id)   # 5 
        print("result_from_db.coordinate ", result_from_db.coordinate) # 010100000097fdbad39d925ec0d00a0c59ddc64240
        print("result_from_db.wkt_shape", result_from_db._wkt_shape)   # None           

        if result_from_db:
            cr_time = result_from_db.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f')

            return location_pb2.LocationMessageResponse(
                id=result_from_db.id,
                person_id=result_from_db.person_id,
                coordinate=result_from_db._wkt_shape,
                creation_time=cr_time)

            # if as is: TypeError: No positional arguments allowed
            # if to_dict(): 	details = "Exception calling application: 'Location' object has no attribute 'to_dict'"
            # added to_dict(): TypeError: 66 has type int, but expected one of: bytes, unicode
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
