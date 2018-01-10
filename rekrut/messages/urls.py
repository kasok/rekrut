from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('<id>/read', views.read, name='read'),
    path('send', views.send, name='send'),
]