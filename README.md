# Petry Auth Backend

Role-based authentication system for managing Superadmin, Executors (ЧСИ), and Assistants using Django and DRF.

## 📦 Features

- ✅ JWT Authentication (Login, Registration, Refresh)
- 👥 Role Management (Superadmin → ЧСИ → Assistant)
- 🌍 Region selection (Kazakhstan)
- 🔐 Role-based permissions
- 📑 Swagger UI Documentation (`/api/docs/`)

## 🚀 Quick Start

```bash
git clone https://github.com/you/petry-auth-backend.git
cd petry-auth-backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔑 Endpoints

| Method | Endpoint                            | Description                   |
| ------ | ----------------------------------- | ----------------------------- |
| POST   | `/api/auth/register/`               | Register new user             |
| POST   | `/api/auth/login/`                  | Obtain JWT tokens             |
| GET    | `/api/auth/me/`                     | Get current user's info       |
| PATCH  | `/api/users/<id>/assign-executor/`  | Assign user as Executor (ЧСИ) |
| PATCH  | `/api/users/<id>/assign-assistant/` | Assign user as Assistant      |

## 🧪 Swagger Docs
- Visit: /api/docs/

## 👤 Roles
- superadmin → can assign Executors
- executor → can assign Assistants
- assistant → data access only