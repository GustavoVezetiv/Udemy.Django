from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_despesas, name='lista_despesas'),
    path('receitas/', views.lista_receitas, name='lista_receitas'),
    path('criar_despesa/', views.criar_despesa, name='criar_despesa'),
    path('criar_receita/', views.criar_receita, name='criar_receita'),  # URL para criar receita
]