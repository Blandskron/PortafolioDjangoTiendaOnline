# tienda/views.py
from django.shortcuts import render
from .models import Producto, Carrito

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    # Obtener el carrito existente o crear uno nuevo si no existe
    carrito, created = Carrito.objects.get_or_create(id=1)  # Asumimos que solo hay un carrito
    
    carrito_item, created = carrito.items.get_or_create(producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    
    carrito.save()
    
    return render(request, 'tienda/agregar_al_carrito.html', {'producto': producto})


def ver_carrito(request):
    carrito = Carrito.objects.first()  # Para simplificar, asumimos que solo hay un carrito
    return render(request, 'tienda/ver_carrito.html', {'carrito': carrito})
