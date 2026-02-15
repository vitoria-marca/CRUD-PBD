# Introdução e Requisitos
Trabalho final para a disciplina de Projeto em Banco de Dados do curso de Bacharelado em Ciência da Computação na UFPel.

Os requisitos do projeto são:
**Python:** 3.8 a 3.10 (Recomendado para compatibilidade com Django 3.2).
**Banco de Dados:** PostgreSQL 9.5.    

## Rodando o projeto
Crie uma pasta com o nome de sua preferência e, no terminal, rode: 

    git clone https://github.com/vitoria-marca/CRUD-PBD.git 
    cd ubs_PBD
Crie o ambiente virtual: 

    python -m venv venv 
    # No Windows: 
    .\venv\Scripts\activate 
    # No Linux/Ubuntu: 
    source venv/bin/activate
 Instale as dependências:

     pip install -r requirements.txt
 Crie um arquivo `.env` na pasta **ubs_core** e insira as seguintes variáveis do seu banco de dados:

    DB_NAME=seu_banco
    DB_USER=seu_user
    DB_PASSWORD=sua_senha
    DB_HOST=127.0.0.1
    DB_PORT=0000

## Utilizando o Jazzmin

Jazzmin possui uma série de estilos em CSS pré-setados, o que facilita o desenvolvimento do front-end da aplicação. Para utilizar, precisamos seguir alguns passos:

    python manage.py collectstatic

## Rodando o projeto

Para utilizar o sistema baseado em django, digite no terminal:

    python manage.py runserver

