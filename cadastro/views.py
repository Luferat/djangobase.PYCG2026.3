from django.shortcuts import render


def index(request):

    contexto = {
        "nome": "Joquinha",
        'idade': 30,
        'frutas': ['Maçã', 'Banana', 'Laranja', 'Uva', 'Cajá', 'Manga'],
        'teste': 'Apenas um <strong>teste para</sctrong> testar'
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
