# tienda/admin.py
from django.contrib import admin
from .models import Producto, CarritoItem, CarritoTotal, Carrito

admin.site.register(Producto)
admin.site.register(CarritoItem)
admin.site.register(CarritoTotal)
admin.site.register(Carrito)
