from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
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
    
class ProductSerializer(serializers.ModelSerializer):
    
    image = serializers.ImageField(write_only=True)
    
    class Meta:
        model = Producto
        fields = ('titulo','descripcion','precio','condicion','fecha','image','cantidad')
        
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