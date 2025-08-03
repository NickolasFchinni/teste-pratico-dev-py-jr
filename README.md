# 📝 Backend - Todo List API

Este projeto é a API do sistema de gerenciamento de tarefas (To-do List), desenvolvida em **Django** com **Django REST Framework**. Ele fornece endpoints autenticados para usuários criarem, atualizarem, deletarem e filtrarem tarefas.

---

## 📦 Requisitos

- Python 3.10+
- pip (gerenciador de pacotes Python)

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório:

```bash
git clone https://github.com/NickolasFchinni/teste-pratico-dev-py-jr.git
cd teste-pratico-dev-py-jr
```

### 2. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 3. Aplique as migrações:

```bash
python manage.py migrate

ou

py manage.py migrate
```

### 4. (Opcional) Crie um superusuário:

```bash
python manage.py createsuperuser

ou

py manage.py createsuperuser
```

### 5. Rode o servidor de desenvolvimento:

```bash
python manage.py runserver

ou

py manage.py runserver
```

A API estará disponível em: [http://localhost:8000/](http://localhost:8000/) ou [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📌 Endpoints Principais

| Método | Endpoint             | Descrição                        |
|--------|----------------------|----------------------------------|
| POST   | `/register/`         | Registro de novo usuário         |
| POST   | `/api-token-auth/`   | Login e obtenção do token        |
| GET    | `/tarefas/`          | Listar tarefas do usuário        |
| POST   | `/tarefas/`          | Criar nova tarefa                |
| GET    | `/tarefas/<id>/`     | Detalhar tarefa específica       |
| PUT    | `/tarefas/<id>/`     | Atualizar tarefa                 |
| DELETE | `/tarefas/<id>/`     | Deletar tarefa                   |

---

## 🔍 Funcionalidades

- Registro e autenticação via Token
- CRUD completo de tarefas
- Filtros por:
  - Status (concluído ou não)
  - Data de criação
- Paginação (5 tarefas por página)
- Proteção de dados: cada usuário acessa apenas suas tarefas

---

## 🧪 Rodando os testes

```bash
pytest
```

## ✅ Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- SQLite (padrão do Django, fácil de usar em dev)
