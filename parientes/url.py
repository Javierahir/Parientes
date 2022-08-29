from django.urls import path
from parientes.views import listar_parientes

urlpatterns = [
    path('parientes/', listar_parientes),
]
