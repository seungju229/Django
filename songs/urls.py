from django.urls import path
from . import views


app_name = 'songs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('update/<int:pk>/', views.update, name = 'update'),
    path('delete/', views.delete, name = 'delete'),
]