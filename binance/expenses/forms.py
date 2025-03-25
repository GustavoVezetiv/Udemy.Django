from django import forms
from .models import Despesa, Receita

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'categoria', 'data', 'receita']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['tipo', 'valor', 'data']