from flask_restful import Resource
from flask import request

class HelloWorld(Resource):
    def get(self):
        return { 'message': 'Hola Mundo desde la API', 'status': 200 }

lista_obj = [
    {
     'id': 1,
     'nombre': 'lapiz',
     'cantidad': 12
     },
    {
     'id': 2,
     'nombre': 'Goma',
     'cantidad': 8
    }, 
    {
     'id': 3,
     'nombre': 'lapicero',
     'cantidad': 7
    }]

class Almacen(Resource):
    def get(self):
        return {'Objetos':lista_obj, 'status': 200}
    
    def post(self):
        data = request.get_json()
        lista_obj.append(data)
        return {'received': True, 'info': data , 'status': 200}

        


class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/Objetos_Almacen')



