from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='tambah'),
    path('daftar/', views.daftar),
]