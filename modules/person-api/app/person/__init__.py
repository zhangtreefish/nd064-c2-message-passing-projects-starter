from app.person.models import Person  # noqa
from app.person.schemas import PersonSchema  # noqa


def register_routes(api, app, root="person-api"):
    from app.person.controllers import api as person_api

    api.add_namespace(person_api, path=f"/{root}")
