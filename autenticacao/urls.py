from django.urls import path, include
from . views import cadastro,logar,sair

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('logar/', logar, name='logar'),
    path('sair/', sair, name="sair"),
]