# Biblioteca-django

## Descrição
Este é um simples projeto de gerenciamento de emprestimo de livros com controle de acesso utilizando login.
## Ferramentas utilizadas
* Django
* Bootstrap
* Sqlite3

## Como rodar localmente
Clene o repositorio
```bash
git clone https://github.com/IgorBarreto/biblioteca-django.git
```
Crie um ambiente virtual
```bash
python -m venv venv
```
Ativar o ambiente virtual 
```bash
venve\Scripts\activate
```
Instalar as bibliotes
```bash
pip install -r requirements.txt
```
Rode as migrações
```bash
python manage.py migrate 
```
Execute o projeto
```bash
python manage.py runserver
```
