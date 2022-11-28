# Biblioteca

## Descrição
Este é um simples projeto de emprestimos de livros com controle de acesso utilizando login.
## Ferramentas utilizadas
* Django
* Bootstrap
* Sqlite3

## Como rodar localmente
Clone o repositorio
```bash
git clone https://github.com/IgorBarreto/biblioteca-django.git
```
Crie um ambiente virtual
```bash
python -m venv venv
```
Ativar o ambiente virtual 
```bash
venv\Scripts\activate
```
Instale as bibliotes
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
