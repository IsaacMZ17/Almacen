from flask import request
from .extensions import db
from .models.producto import Producto

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