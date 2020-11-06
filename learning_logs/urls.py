"""Define padrões de URL para learning_logs"""

from . import views 
from django.urls import path, include

urlpatterns = [
    #Página Inicial
    path('', views.index, name='index'),

    #Página de tópicos
    path('topics', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic')
]
