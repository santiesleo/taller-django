from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('nuevo/', views.nuevo_articulo, name='nuevo_articulo'),
]