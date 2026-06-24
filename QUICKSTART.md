# HackXHarder - Quick Start (Local Dev)

**Setup**: Backend + Frontend + PostgreSQL on your PC. Only Redis via Docker (optional).

---

## 30-Second Setup

### 1. Start Redis (Docker)
```bash
docker-compose up -d redis
```

### 2. Backend (Terminal 1)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env - set DB_HOST=localhost, DB_USER, DB_PASSWORD
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Backend: http://localhost:8000
API Docs: http://localhost:8000/api/v1/docs/

### 3. Celery Worker (Terminal 2)
```bash
cd backend
source venv/bin/activate
celery -A config worker -l info
```

### 4. Frontend (Terminal 3)
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

Frontend: http://localhost:3000

---

## Prerequisites

- **Python 3.10+** (`python --version`)
- **Node.js 18+** (`node --version`)
- **PostgreSQL 15** running locally
- **Docker** (optional, for Redis)

---

## PostgreSQL Setup

### Create Database & User

```bash
psql -U postgres

CREATE DATABASE hackxharder_db;
CREATE USER hackxharder WITH PASSWORD 'password123';

ALTER ROLE hackxharder SET client_encoding TO 'utf8';
ALTER ROLE hackxharder SET default_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE hackxharder_db TO hackxharder;

\q
```

Update `.env`:
```
DB_HOST=localhost
DB_USER=hackxharder
DB_PASSWORD=password123
DB_NAME=hackxharder_db
```

---

## Full Process

**5 Terminals**:

1. **Redis**: `docker-compose up -d redis`
2. **PostgreSQL**: Ensure running (`sudo systemctl start postgresql` or service equivalent)
3. **Backend**: `cd backend && python manage.py runserver`
4. **Celery**: `cd backend && celery -A config worker -l info`
5. **Frontend**: `cd frontend && npm run dev`

---

## Environment Files

### Backend (`.env`)
```
DEBUG=True
SECRET_KEY=dev-key-12345
DB_HOST=localhost
DB_USER=hackxharder
DB_PASSWORD=password123
DB_NAME=hackxharder_db
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (`.env.local`)
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_ENVIRONMENT=development
```

---

## Common Commands

| Task | Command |
|------|---------|
| Start PostgreSQL | `sudo systemctl start postgresql` (or service) |
| Start Redis | `docker-compose up -d redis` |
| Backend migrations | `cd backend && python manage.py migrate` |
| Create superuser | `cd backend && python manage.py createsuperuser` |
| Run backend | `cd backend && python manage.py runserver` |
| Run Celery | `cd backend && celery -A config worker -l info` |
| Run frontend | `cd frontend && npm run dev` |
| Backend tests | `cd backend && pytest` |
| Frontend tests | `cd frontend && npm test` |

---

## API & Dashboard

- **API Docs (Swagger)**: http://localhost:8000/api/v1/docs/
- **Admin Panel**: http://localhost:8000/admin/
- **Frontend**: http://localhost:3000/

---

## Next Steps

1. Create user accounts (register or use admin panel)
2. Create program (company admin)
3. Submit report (researcher)
4. Triage & approve (triage lead)
5. View bounty (researcher)

See `docs/LOCAL_SETUP.md` for detailed setup + troubleshooting.
