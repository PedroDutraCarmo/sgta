from django.urls import path
from .views import Listar_tarefas, listar_tarefas_abertas

urlpatterns = [
    path("tarefas/", Listar_tarefas),
    path('tarefas/abertas/', listar_tarefas_abertas),
]