from django.urls import path
from.views import listar_pessoas, criar_pessoa

urlpatterns = [
    path('listar/', listar_pessoas, name = 'listar_pessoas'),
    path('criar', criar_pessoas, name = 'criar_pessoa'),
]