from django.db import models
from django.contrib.auth.models import User


ESTADOS_TRANSACCION = (
    ('pendiente', 'Pendiente'),
    ('completada', 'Completada'),
    ('cancelada', 'Cancelada'),
)

class Categoria(models.Model):
    id_categoria=models.IntegerField(primary_key=True)
    categoria=models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria

class Producto(models.Model):
    id_producto=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    condicion=models.CharField(max_length=50)
    fecha=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='static/img/', height_field=None, width_field=None, max_length=None)
    cantidad=models.IntegerField()
    precio=models.FloatField()
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Transaccion(models.Model):
    id_transaccion=models.IntegerField(primary_key=True)
    id_comprador=models.ForeignKey(User, on_delete=models.CASCADE, related_name='compra')
    id_vendedor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='venta')
    id_producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_transaccion=models.DateField(auto_now=True)
    precio_transaccion=models.FloatField()
    estado = models.CharField(max_length=20, choices=ESTADOS_TRANSACCION)    
    def __str__(self):
        return self.estado



