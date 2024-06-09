#API RESTful: Crea una API RESTful utilizando un framework como Flask o Django Rest Framework. Puedes construir una API para cualquier propósito, como
#gestionar datos de usuarios, productos, o servicios.
from fastapi import FastAPI 
from esquema.modelo import Productos

app = FastAPI()

productos = [
    {
        "id" : 1 ,
        "nombre" : "jarron",
        "año" : 1489
    }
]



@app.get('/')

def mensaje():
    return ("Hola hijos de perra!")


@app.get('/productos')

def producto():
    return productos


#id productos
@app.get('/productos/{id}')

def get_producto(id: int):
    return list(filter(lambda item: item["id"] == id ,productos))


@app.get('/productos/')
def get_producto_nombre(nombre : str, año: int):
    return list(filter(lambda item: item["nombre"] == nombre and item["año"] == año ,productos))


@app.post('/productos')
def crear_producto(product: Productos):
    productos.append(product)
    return productos


@app.put('/productos/{id}')
def actualizar_datos(id: int , product : Productos):
    for index , item in enumerate(productos):
        if item['id'] == id:
            productos[index]['name'] = product.nombre
            productos[index]['año'] = product.año


    return productos


@app.delete('/products/{id}')
def delete_products(id: int):
    for item in productos:
        if item['id'] == id:
            productos.remove(item)

    return productos












