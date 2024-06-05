from flask import request

def BuscarElemento (lista ,id, nombre):
    if id != None:
        for objeto in lista: 
            if objeto.get('id') == int(id):
                return {'Objeto': objeto, 'status': 200}

        return {'Mensaje': 'Objeto no encontrado', 'status': 404}
        
    if nombre != None:
        for objeto in lista: 
            if objeto.get('nombre') == nombre:
                return {'Objeto': objeto, 'status': 200}

        return {'Mensaje': 'Objeto no encontrado', 'status': 404}
           
    return {'Objetos':lista, 'status': 200}