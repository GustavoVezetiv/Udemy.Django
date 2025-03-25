from django.shortcuts import render, redirect
from .models import Despesa, Receita
from .forms import DespesaForm, ReceitaForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def lista_despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'expenses/expense_list.html', {'despesas': despesas})

def lista_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'expenses/receita_list.html', {'receitas': receitas})

def criar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_despesas')
    else:
        form = DespesaForm()
    return render(request, 'expenses/criar_despesa.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ReceitaForm

def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_receitas')  # Certifique-se de que esta URL está configurada
    else:
        form = ReceitaForm()
    return render(request, 'expenses/criar_receita.html', {'form': form})

def grafico_entradas_saidas(request):
    receitas = Receita.objects.all()
    despesas = Despesa.objects.all()

    receita_total = sum(receita.valor for receita in receitas)
    despesa_total = sum(despesa.valor for despesa in despesas)

    fig, ax = plt.subplots()
    ax.bar(['Receitas', 'Despesas'], [receita_total, despesa_total])
    ax.set_ylabel('Valor')
    ax.set_title('Entradas e Saídas')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'expenses/grafico.html', {'graphic': graphic})


from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'expenses/pagina_inicial.html')
