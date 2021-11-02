def register_routes(api, app, root="person-api"):
    from app.person import register_routes as attach_person

    # Add routes
    attach_person(api, app)
