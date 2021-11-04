import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.person.models import Person
from app.person.schemas import PersonSchema

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("person-api")

class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()

    @staticmethod
    def retrieve_all_persons() -> List[Person]:
        return [
        {"id": 1, "first_name": "John", "last_name":"smith", "company_name": "udacity"},
        {"id": 5, "first_name": "she", "last_name":"whom", "company_name": "tesla"},     
    ]

    @staticmethod
    def retrieve_one(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return {"id": 1, "first_name": "the", "last_name":"only", "company_name": "one"}
