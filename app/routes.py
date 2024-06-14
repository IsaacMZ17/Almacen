from flask_restful import Resource
from flask import request
from .methods import *

class HelloWorld(Resource):
    def get(self):
        return { 'message': 'Hola Mundo desde la API', 'status': 200 }

class Almacen(Resource):
    def get(self):
        id = request.args.get('id')
        nombre = request.args.get('nombre')
        return BuscarElemento(id, nombre)
    
    def post(self):
        data = request.get_json()
        
        return crear_producto(data['nombre'], data['cantidad'])


class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/Objetos_Almacen')
