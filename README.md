# djangobase
Primeiros experimentos com Django da turma PYCG2026.3.

# Atividade Desafio

Deixe a página / rota `http://localhost:8000/contato/`funcional, apresentando um formulário com os campos:

 - `nome`
 - `email`
 - `assunto`
 - `mensagem`

Quando o formulário for enviado, salva esses dados no banco de dados em um tabela `Contato`.

## Dica de sequência

1. `models.py` → Modele a tabela criando os campos
2. `admin.py` → Adicione contatos ao **Django Admin**
3. `urls.py` → Apenas verifique a rota para contatos
4. `forms.py` → Modele o formulário de contatos
5. `views.py` → Descreva a lógica dos contatos

