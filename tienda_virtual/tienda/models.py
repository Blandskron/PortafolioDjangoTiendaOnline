# tienda/models.py
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

class CarritoTotal(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

class Carrito(models.Model):
    items = models.ManyToManyField(CarritoItem)

    def __str__(self):
        return f"Carrito {self.id}"

    def total_carrito(self):
        total = sum(item.producto.precio * item.cantidad for item in self.items.all())
        return total

    def total_items(self):
        total = sum(item.cantidad for item in self.items.all())
        return total
