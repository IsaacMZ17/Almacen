from flask_restful import Resource
from flask import request
from .methods import *

lista_obj = [
    {
     'id': 1,
     'nombre': 'lapiz',
     'cantidad': 12
     },
    {
     'id': 2,
     'nombre': 'goma',
     'cantidad': 8
    }, 
    {
     'id': 3,
     'nombre': 'lapicero',
     'cantidad': 7
    }]

class HelloWorld(Resource):
    def get(self):
        return { 'message': 'Hola Mundo desde la API', 'status': 200 }

class Almacen(Resource):
    def get(self):
        id = request.args.get('id')
        nombre = request.args.get('nombre')
        return BuscarElemento(lista_obj, id, nombre)
    
    def post(self):
        data = request.get_json()
        lista_obj.append(data)
        return {'received': True, 'info': data , 'status': 200}


class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/Objetos_Almacen')
