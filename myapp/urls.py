from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='Todos'),
    path('preview_image/<str:filename>/', views.preview_image, name='preview_image'),
]
