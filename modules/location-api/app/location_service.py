import logging
from datetime import datetime, timedelta
from typing import Dict, List

from models import Location
from schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from database import db  # noqa


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location_service")

class LocationService:
    @staticmethod
    def Retrieve(location_id) -> Location:
        with db.Session() as dbs: # work with the session here
            """ location, coord_text = (
                dbs.query(Location, Location.coordinate.ST_AsText())
                .filter(Location.id == location_id)
                .one()
            ) """
            attr = {"id": 66}
            location = db.s.first(Location, **attr)
            # Rely on database to return text form of point to reduce overhead of conversion in app code
            # location.wkt_shape = coord_text
            return location

    @staticmethod
    def Create(location: Dict) -> Location:
        # print("location in svc:", location)
        # location_dt = datetime.fromtimestamp(location['creation_time'])
        # location_payload = {"creation_time": datetime.fromtimestamp(location['creation_time']['seconds'] + location['creation_time']['nanos'] / 1e9)}
        # location_payload =  {"creation_time": location_dt}
        # location.update(location_payload)
        print("location in svc: before validate = ", location)
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        # new_location_dict = new_location.__dict__

        result = {}
        with db.Session() as dbs: # work with the session here
            persisted_location = db.s.add(new_location)
            result = persisted_location
            db.s.flush()
            db.s.commit()
            return result

        return result   

