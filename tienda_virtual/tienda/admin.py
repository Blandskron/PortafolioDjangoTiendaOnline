# tienda/admin.py
from django.contrib import admin
from .models import Producto, CarritoItem, Carrito

admin.site.register(Producto)
admin.site.register(CarritoItem)
admin.site.register(Carrito)
