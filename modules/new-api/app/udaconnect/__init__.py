from app.common.models import Connection, Location # noqa
from app.common.schemas import ConnectionSchema, LocationSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
