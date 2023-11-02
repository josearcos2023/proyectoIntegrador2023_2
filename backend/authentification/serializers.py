from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ProductSerializer(ModelSerializer):
    
    image = serializers.ImageField(write_only=True)
    
    class Meta:
        model = Producto
        fields = ('id_producto','titulo','descripcion','precio','condicion','fecha','image','cantidad')
        
    def create(self, validated_data):
        image = validated_data.pop('image')
        producto = Producto.objects.create(
            titulo=validated_data['titulo'],
            descripcion=validated_data['descripcion'],
            precio=validated_data['precio'],
            condicion=validated_data['condicion'],
            fecha=validated_data['fecha'],
            image=validated_data['image'],
            cantidad=validated_data['cantidad'],
        )
        
        producto.image = image
        producto.save()
        
        return producto
    
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_categoria', 'categoria')

class TransaccionSerializer(ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ('id_transaccion', 'id_comprador', 'id_vendedor', 'id_producto', 'fecha_transaccion', 'precio_transaccion', 'estado')