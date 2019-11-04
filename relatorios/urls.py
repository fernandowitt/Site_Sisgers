from django.urls import path
from . import views


urlpatterns = [
    path('todasvistorias', views.todasvistorias, name='todasvistorias'),
    path('', views.minhasvistorias, name='minhasvistorias'),
    path('vistoria/<int:pk>', views.vistoriadetalhes, name='vistoriadetalhes'),
]
