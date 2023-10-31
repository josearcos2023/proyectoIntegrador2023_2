from django.contrib import admin
from .models import Categoria, Producto, Transaccion

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'titulo','condicion','fecha','cantidad','precio') 
    list_filter = ('condicion', 'fecha')
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'categoria') 

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id_transaccion', 'id_comprador','id_vendedor','estado') 

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Transaccion,TransaccionAdmin)