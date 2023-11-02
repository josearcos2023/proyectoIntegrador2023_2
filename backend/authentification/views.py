from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import UserSerializer,ProductSerializer,CategoriaSerializer,TransaccionSerializer
from .models import *
  
class HomeView(APIView):
    permission_classes = (IsAuthenticated,)
  
    def get(self, request):
        content = {'message': 'LANDING PAGE!'}
        return Response(content)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# rest productos    
class ProductosView(APIView):
    
    def get(self,request):
        dataProductos = Producto.objects.all()
        serProductos = ProductSerializer(dataProductos,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProducto = ProductSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)

class ProductoDetailView(APIView):
    
    def get(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)
    

# api rest categoria

class CategoriasView(APIView):
    
    def get(self,request):
        dataCategorias = Categoria.objects.all()
        serCategorias = CategoriaSerializer(dataCategorias,many=True)
        return Response(serCategorias.data)
    
    def post(self,request):
        serCategoria = CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        
        return Response(serCategoria.data)
    
class CategoriaDetailView(APIView):
    
    def get(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        return Response(serCategoria.data)
    
    def put(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria,data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)
    
    def delete(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        dataCategoria.delete()
        return Response(serCategoria.data)


class TransaccionsView(APIView):
    
    def get(self,request):
        dataTransaccions = Transaccion.objects.all()
        serTransaccions = TransaccionSerializer(dataTransaccions,many=True)
        return Response(serTransaccions.data)
    
    def post(self,request):
        serTransaccion = TransaccionSerializer(data=request.data)
        serTransaccion.is_valid(raise_exception=True)
        serTransaccion.save()
        
        return Response(serTransaccion.data)
    
class TransaccionDetailView(APIView):
    
    def get(self,request,transaccion_id):
        dataTransaccion = Transaccion.objects.get(pk=transaccion_id)
        serTransaccion = TransaccionSerializer(dataTransaccion)
        return Response(serTransaccion.data)
    
    def put(self,request,transaccion_id):
        dataTransaccion = Transaccion.objects.get(pk=transaccion_id)
        serTransaccion = TransaccionSerializer(dataTransaccion,data=request.data)
        serTransaccion.is_valid(raise_exception=True)
        serTransaccion.save()
        return Response(serTransaccion.data)
    
    def delete(self,request,transaccion_id):
        dataTransaccion = Transaccion.objects.get(pk=transaccion_id)
        serTransaccion = TransaccionSerializer(dataTransaccion)
        dataTransaccion.delete()
        return Response(serTransaccion.data)
