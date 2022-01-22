from django.urls import path, include

from producto import views

urlpatterns = [
    path('', views.AllProductsList.as_view()),
    path('ultimos-productos/', views.UltimosProductosList.as_view()),
    path('categoria/', views.CategoriaList.as_view()),
    path('busqueda/', views.busqueda),
    path('<slug:categoria_slug>/<slug:producto_slug>/', views.ProductoDetalles.as_view()),
    path('<slug:categoria_slug>/', views.CategoriaDetalles.as_view()),
]