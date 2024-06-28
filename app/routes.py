from flask_restful import Resource
from flask import request
from .methods import *
from flask_jwt_extended import jwt_required, get_jwt_identity #type: ignore

class HelloWorld(Resource):
    @jwt_required()
    def get(self):
        identidad = get_jwt_identity()
        return { 'message': f'Hola {identidad}, ¿Como estas?', 'status': 200 }

class Almacen(Resource):
    def get(self):
        id = request.args.get('id')
        nombre = request.args.get('nombre')
        return BuscarElemento(id, nombre)
    
    def post(self):
        data = request.get_json()
        
        return crear_producto(data['nombre'], data['cantidad'])

class User_register(Resource):
    def post(self):
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        respuesta, status = user_register(username, email, password)

        return respuesta, status

class User_login(Resource):
    def post(self):
        data = request.form
        email = data.get('email')
        password = data.get('password')
        
        respuesta, status = inicio_sesion(email, password)

        return respuesta, status

class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(User_login, '/usuarios/login')
        api.add_resource(User_register, '/usuarios/registro')
        api.add_resource(Almacen, '/Objetos_Almacen')
