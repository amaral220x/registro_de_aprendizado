"""Define padrões de URL para learning_logs"""

from . import views 
from django.urls import path, include

urlpatterns = [
    #Página Inicial
    path('', views.index, name='index'),
]