from django.urls import path
from . import views
  
urlpatterns = [
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),   
    path('register/', views.RegisterView.as_view(), name='productos'),
    path('producto',views.ProductosView.as_view(),name='producto'),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
    path('categoria',views.CategoriasView.as_view(),name='categoria'),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('transaccion',views.TransaccionsView.as_view(),name='transaccion'),
    path('transaccion/<int:transaccion_id>',views.TransaccionDetailView.as_view()),

]