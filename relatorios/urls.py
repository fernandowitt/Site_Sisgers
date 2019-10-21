from django.urls import path
from . import views


urlpatterns = [
    path('', views.telainicial, name='telainicial'),
    path('minhasvistorias', views.minhasvistorias, name='minhasvistorias'),
    path('vistoria/<int:pk>', views.vistoriadetalhes, name='vistoriadetalhes'),
]
