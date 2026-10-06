from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.index, name='index'),

    # Rota da página "Contatos"
    path('contato/', views.contato, name='contato')
]