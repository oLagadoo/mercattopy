from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('categorias/', views.category_list, name='category_list'),
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/novo/', views.product_create, name='product_create'),
    path('produtos/<int:pk>/editar/', views.product_update, name='product_update'),
    path('produtos/<int:pk>/excluir/', views.product_delete, name='product_delete'),
    path('produtos/<int:pk>/', views.product_detail, name='product_detail'),
    path('logout/', views.logout_view, name='logout'),
]