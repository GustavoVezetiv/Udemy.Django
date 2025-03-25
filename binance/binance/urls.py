from django.contrib import admin
from django.urls import path, include
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('despesas/', include('expenses.urls')),
    path('', views.pagina_inicial, name='pagina_inicial'),  # Adicionada a rota para a página inicial
]
