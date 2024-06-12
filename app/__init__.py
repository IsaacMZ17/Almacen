from flask import Flask
from flask_restful import Api
from .routes import Resource
from .routes import APIRoutes
from .config import Config
from .extensions import db

def crear_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

        api = Api(app)

        routes= APIRoutes()
        routes.init_routes(api)
    return app