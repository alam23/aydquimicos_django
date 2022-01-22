from django.urls import path, include

from producto import views

urlpatterns = [
    path('todos-productos/', views.AllProductsList.as_view()),
    path('ultimos-productos/', views.UltimosProductosList.as_view()),
    path('categorias/', views.CategoriaList.as_view()),
    path('crear-categoria/', views.createCategory),
    path('actualizar-categoria/<str:pk>/', views.updateCategory),
    path('eliminar-categoria/<str:pk>/', views.deleteCategory),
    path('busqueda/', views.busqueda),
    path('crear-producto/', views.createProduct),
    path('<slug:categoria_slug>/<slug:producto_slug>/', views.ProductoDetalles.as_view()),
    path('<slug:categoria_slug>/', views.CategoriaDetalles.as_view()),
]