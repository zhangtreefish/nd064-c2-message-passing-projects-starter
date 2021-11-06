def register_routes(api, app, root="api"):
    from app.udaconnect import register_routes as attach_udaconnect
    from app.persons import register_routes as attach_persons

    # Add routes
    attach_udaconnect(api, app)
    attach_persons(api, app)