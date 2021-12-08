### Ambiente

#### Criando ambiente virtual
    python -m venv venv

#### Acessando o ambiente virtual
    .\venv\Scripts\activate

#### Instalando o Django
    pip install django

#### Criando aplicativo
    django-admin startproject blog_do_joca
    cd blog_do_joca

#### Executando o servidor local
    python manage.py runserver

### Migrations

#### Consultando uma migration --> Ex.: 'auth'
    python manage.py sqlmigrate auth 0001

#### Status das migrations
    python manage.py show migrations

#### Criando bancos de dados
    python manage.py migrate

### Aplicativo

#### Criando um app no projeto
    python manage.py startapp blog

#### Criando e consultando a migration do app --> ./blog/models.py
    python manage.py makemigrations blog
    python manage.py sqlmigrate blog 0001
    python manage.py migrate blog

### Admin

#### Criando administrador do Django Admin --> admin | Q1w2e3r4t5
    python manage.py createsuperuser

#### Acessando o Django Admin
    http://localhost:8000/admin