# Tienda Virtual en Django

Este es un proyecto de tienda virtual desarrollado con Django, un framework web de alto nivel y de código abierto en Python.

## Descripción

El objetivo de este proyecto es crear una plataforma básica de comercio electrónico donde los usuarios puedan ver una lista de productos, ver detalles de un producto específico, agregar productos a un carrito de compras y ver el contenido del carrito con la cantidad total de productos y el monto total a pagar.

## Funcionalidades

- Lista de productos: Los usuarios pueden ver una lista de todos los productos disponibles en la tienda.
- Detalle de producto: Los usuarios pueden ver los detalles de un producto específico, incluyendo su nombre, descripción y precio.
- Agregar al carrito: Los usuarios pueden agregar productos al carrito de compras.
- Ver carrito: Los usuarios pueden ver el contenido del carrito de compras, incluyendo la cantidad total de productos y el monto total a pagar.

## Configuración del Proyecto

1. Clona este repositorio en tu máquina local:

```
git clone <URL del repositorio>
```

Instala las dependencias del proyecto:
```
pip install -r requirements.txt
```
Realiza las migraciones de la base de datos:
```
python manage.py migrate
```
Inicia el servidor de desarrollo:
```
python manage.py runserver
```
Abre tu navegador web y ve a http://127.0.0.1:8000/tienda/ para ver la tienda virtual.
