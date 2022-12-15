from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.userPage, name='user-page'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create-order/<str:pk>/', views.create_order, name='create-order'),
    path('update-order/<str:pk>/', views.update_order, name='update-order'),
    path('delete-order/<str:pk>/', views.delete_order, name='delete-order'),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'), 
]
