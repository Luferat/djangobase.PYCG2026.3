from django.shortcuts import get_object_or_404, redirect, render

from cadastro.forms import PessoaForm
from cadastro.models import Pessoa


def index(request):

    # Recebe todas as "Pessoas" do banco de dados
    pessoas = Pessoa.objects.order_by('nome', 'email')

    # Conta o total de registros
    total = Pessoa.objects.count()

    contexto = {
        'nome': 'Joquinha',
        'pessoas': pessoas,
        'total': total
    }

    return render(
        request,
        'cadastro/index.html',
        contexto
    )


def contato(request):

    contexto = {
        "nome": "Joquinha"
    }

    return render(
        request,
        'cadastro/contato.html',
        contexto
    )


def adicionar(request):
    # Se o form está sendo enviado
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # Exibe o formulário
        form = PessoaForm()

    return render(
        request,
        'cadastro/adicionar.html',
        {'form': form, 'nome': 'Joquinha'}
    )


def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(
        request,
        'cadastro/detalhe.html',
        {
            'pessoa': pessoa,
            'nome': 'Joquinha'
        }
    )


def editar(request, id):

    # Obtém os dados da pessoa pelo ID
    pessoa = get_object_or_404(Pessoa, id=id)

    # Se o frmulário foi enviado
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(
        request,
        'cadastro/editar.html',
        {
            'form': form,
            'pessoa': pessoa,
            'nome': 'Joquinha'
        }
    )


def deletar(request, id):

    # Obtém os dados da pessoa pelo ID
    pessoa = get_object_or_404(Pessoa, id=id)

    # Se o frmulário foi enviado
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')

    return render(
        request,
        'cadastro/deletar.html',
        {
            'pessoa': pessoa,
            'nome': 'Joquinha'
        }
    )
