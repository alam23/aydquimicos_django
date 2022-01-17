from django.urls import path, include

from producto import views

urlpatterns = [
    path('ultimos-productos/', views.UltimosProductosList.as_view()),
    path('productos/busqueda/', views.busqueda),
    path('productos/<slug:categoria_slug>/<slug:producto_slug>/', views.ProductoDetalles.as_view()),
    path('productos/<slug:categoria_slug>/', views.CategoriaDetalles.as_view()),
]