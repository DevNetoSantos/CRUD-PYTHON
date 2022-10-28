from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:id>/details', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('user/<int:id>/delete/', views.delete, name='delete'),
    path('user/<int:id>/update/', views.update, name='update')
]
