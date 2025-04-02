from django.urls import path, include
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('payment_success/', views.payment_success, name='payment_success'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm/', views.confirm_order, name='confirm_order'),
    path('process_order/', views.process_order, name='process_order'),
]
