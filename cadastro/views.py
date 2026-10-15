# cadastro\views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cadastro.forms import ContatoForm, PessoaForm
from cadastro.models import Pessoa
from django.contrib import messages
from django.utils.safestring import mark_safe

def index(request):

    # Recebe todas as "Pessoas" do banco de dados
    pessoas = Pessoa.objects.order_by('nome', 'email')

    # Conta o total de registros
    total = Pessoa.objects.count()

    contexto = {
        'pessoas': pessoas,
        'total': total
    }

    return render(
        request,
        'cadastro/index.html',
        contexto
    )


def contato(request):

    # Se o form está sendo enviado
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato enviado com sucesso!')
            return redirect('index')
    else:
        # Exibe o formulário
        form = ContatoForm()

    return render(
        request,
        'cadastro/contato.html',
        {'form': form}
    )


@login_required
def adicionar(request):
    # Se o form está sendo enviado
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                mark_safe(
                    f'<strong>{form["nome"].value()}</strong> adicionada(o) com sucesso!')
            )
            return redirect('index')
    else:
        # Exibe o formulário
        form = PessoaForm()

    return render(
        request,
        'cadastro/adicionar.html',
        {'form': form}
    )


def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(
        request,
        'cadastro/detalhe.html',
        {'pessoa': pessoa}
    )


@login_required
def editar(request, id):

    # Obtém os dados da pessoa pelo ID
    pessoa = get_object_or_404(Pessoa, id=id)

    # Se o frmulário foi enviado
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                mark_safe(
                    f'<strong>{form["nome"].value()}</strong> edita(o) com sucesso!')
            )
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(
        request,
        'cadastro/editar.html',
        {
            'form': form,
            'pessoa': pessoa
        }
    )


@login_required
def deletar(request, id):

    # Obtém os dados da pessoa pelo ID
    pessoa = get_object_or_404(Pessoa, id=id)

    # Se o frmulário foi enviado
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Pessoa deletada com sucesso!')
        return redirect('index')

    return render(
        request,
        'cadastro/deletar.html',
        {'pessoa': pessoa}
    )
