from django.urls import path

from orden import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('ordenes/', views.OrdersList.as_view()),  
]