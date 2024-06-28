from flask import request
from .extensions import db
from .models.producto import Producto
from .models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def inicio_sesion(email, password):
    user = User.get_user_by_email(email=email)

    caducidad = timedelta(minutes=2)

    if user and (User.check_password(password=password)):
        token_acceso = create_access_token(identity = user.username, expires_delta= caducidad)
        return { 'Mensaje': 'Logeado',
                 'Token': token_acceso
                }, 200

    return { 'Error': 'Correo o contraseñan no existen :(' }, 400


def user_register (username, email, password):

    user = User.get_user_by_email(email=email)

    if user is not None:
        return { 'Error': 'Este correo ya esta registrado :(' }, 403
    
    nuevo_usuario = User(username=username, email=email)
    nuevo_usuario.set_password(password=password)
    nuevo_usuario.save()

    return { 'Nuevo usuario': {
        'email': email,
        'username': username
      } 
    }, 200

def BuscarElemento (id, nombre):
    if id != None:
        producto_obtenido = Producto.query.get_or_404(id)

        json_retornado = {
            'ID': producto_obtenido.id,
            'Nombre': producto_obtenido.nombre,
            'Cantidad': producto_obtenido.cantidad
        }

        return json_retornado
    
    elif nombre != None:
        producto_obtenido = Producto.query.filter_by(nombreF=nombre).first_or_404(nombre)

        json_retornado = {
            'ID': producto_obtenido.id,
            'Nombre': producto_obtenido.nombre,
            'Cantidad': producto_obtenido.cantidad
        }

        return json_retornado
    
    else:
        return {'Error': 'No Query'}
    
def crear_producto(nombre, cantidad):
    nuevo_producto = Producto(nombre=nombre, cantidad=cantidad)
    db.session.add(nuevo_producto)
    db.session.commit()
    json_retornado = {
            'ID': nuevo_producto.id,
            'Nombre': nuevo_producto.nombre,
            'Cantidad': nuevo_producto.cantidad
        }

    return json_retornado