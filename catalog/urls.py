from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categorias/', views.category_list, name='category_list'),
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/<int:pk>/', views.product_detail, name='product_detail'),
    path('logout/', views.logout_view, name='logout'),
]