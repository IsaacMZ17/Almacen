from flask import Flask
from flask_restful import Api
from .routes import Resource
from .routes import APIRoutes

def crear_app():
    app = Flask(__name__)
    api = Api(app)

    routes= APIRoutes()
    routes.init_routes(api)
    return app

