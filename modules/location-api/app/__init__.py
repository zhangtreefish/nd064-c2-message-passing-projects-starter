from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# adapted from other __init__.py, removing api parts
def create_app(env=None):
    from location.config import config_by_name

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    
    with app.app_context():
        # init_db()
        db.init_app(app)

    return app
    