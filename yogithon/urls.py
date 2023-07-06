from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.main, name="home"),
    path('<str:id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/delete/', views.delete, name="delete"),
]