from django.urls import path, include
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('category/<str:name>', views.category, name='category'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/update_user/', views.update_user, name='update'),
    path('profile/update_info/', views.update_info, name='update_info'),
    path('update_passsword/', views.update_password, name='update_password'),
    path('signup/', views.signup_user, name='signup'),
    path('product/<int:pk>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('profile/orders/', views.orders, name='orders'),
    path('profile/order_details/<int:pk>/<int:num>/', views.order_details, name='order_details'),
]
