# Notas por Cidade

Sistema web em Django para cadastrar, pesquisar e visualizar notas associadas a cidades.

## Tecnologias

- Python
- Django
- SQLite
- Pandas
- HTML/CSS
- Bootstrap 5
- Chart.js

## Funcionalidades

- Lista de notas por cidade
- Pesquisa por nome, cidade e curso
- Filtro por cidade
- Ordenação por nota
- Estatísticas de média, maior e menor nota
- Gráfico das maiores notas
- Área administrativa para cadastrar/editar registros
- Importação de CSV pelo Django Admin

## Formato do CSV

```csv
nome,cidade,estado,curso,nota,ano
João Silva,Barra do Garças,MT,Medicina,782.50,2026
Maria Souza,Cuiabá,MT,Medicina,801.20,2026
```

## Como executar

### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## GitHub

```bash
git init
git add .
git commit -m "Primeira versão do sistema de notas por cidade"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/notas-por-cidade.git
git push -u origin main
```

> Troque a URL do `origin` pela URL do seu repositório.
