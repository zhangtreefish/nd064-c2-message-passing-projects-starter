from app.common.models import Person  # noqa
from app.common.schemas import PersonSchema  # noqa


def register_routes(api, app, root="persons-api"):
    from app.persons.controllers import api as persons_api

    api.add_namespace(persons_api, path=f"/{root}")
