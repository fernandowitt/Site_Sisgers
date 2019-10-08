from django.urls import path
from . import views


urlpatterns = [
    path('loginmobile/', views.loginmobile, name='loginmobile'),
    path('cadastrovistoria/', views.cadastrovistoria, name='cadastrovistoria')
]
