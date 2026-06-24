# Local Development Setup (No Docker)

**Environment**: Backend + Frontend + PostgreSQL run on local PC. Only Redis via Docker (optional).

---

## Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Git
- Redis (via Docker OR installed locally)

---

## 1. PostgreSQL Setup (Local)

### Option A: Install PostgreSQL Locally

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

**macOS (Homebrew)**:
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Windows**:
Download from https://www.postgresql.org/download/windows/

### Create Database & User

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE hackxharder_db;

# Create user
CREATE USER hackxharder WITH PASSWORD 'your_secure_password';

# Grant privileges
ALTER ROLE hackxharder SET client_encoding TO 'utf8';
ALTER ROLE hackxharder SET default_transaction_isolation TO 'read committed';
ALTER ROLE hackxharder SET default_transaction_deferrable TO on;
ALTER ROLE hackxharder SET default_transaction_read_committed TO on;
GRANT ALL PRIVILEGES ON DATABASE hackxharder_db TO hackxharder;

# Quit
\q
```

---

## 2. Redis Setup (Docker Optional)

### Option A: Docker (Recommended for Dev)

```bash
docker run -d -p 6379:6379 --name hackxharder-redis redis:7
```

Check it's running:
```bash
redis-cli ping
# Output: PONG
```

### Option B: Install Redis Locally

**Ubuntu/Debian**:
```bash
sudo apt install redis-server
sudo systemctl start redis-server
```

**macOS**:
```bash
brew install redis
brew services start redis
```

**Windows**: Use WSL2 or https://github.com/microsoftarchive/redis/releases

---

## 3. Backend Setup

### Clone & Navigate
```bash
cd hackxharder/backend
```

### Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment

Copy `.env.example` → `.env`:
```bash
cp .env.example .env
```

Edit `.env`:
```
DEBUG=True
SECRET_KEY=dev-secret-key-12345-change-in-production
DB_HOST=localhost
DB_USER=hackxharder
DB_PASSWORD=your_secure_password
DB_NAME=hackxharder_db
DB_PORT=5432
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2
CORS_ALLOWED_ORIGINS=http://localhost:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser (Admin)

```bash
python manage.py createsuperuser
# Follow prompts
```

### Run Backend Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Backend accessible at: **http://localhost:8000**
Admin panel: **http://localhost:8000/admin**
API docs: **http://localhost:8000/api/v1/docs/**

---

## 4. Frontend Setup

### Navigate to Frontend
```bash
cd ../frontend  # or /path/to/hackxharder/frontend
```

### Install Dependencies
```bash
npm install
```

### Configure Environment

Copy `.env.local.example` → `.env.local`:
```bash
cp .env.local.example .env.local
```

Edit `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_APP_NAME=HackXHarder
NEXT_PUBLIC_ENVIRONMENT=development
```

### Run Frontend Dev Server

```bash
npm run dev
```

Frontend accessible at: **http://localhost:3000**

---

## 5. Celery Worker (Background Jobs)

### Terminal 1: Already Running Backend

Keep `python manage.py runserver` running.

### Terminal 2: Run Celery Worker

```bash
cd backend
source venv/bin/activate
celery -A config worker -l info
```

---

## Full Local Dev Workflow

**Terminal 1 - Redis** (if using Docker):
```bash
docker run -d -p 6379:6379 --name hackxharder-redis redis:7
```

**Terminal 2 - PostgreSQL** (if installed locally):
```bash
# Just ensure PostgreSQL service is running
sudo systemctl status postgresql  # or equivalent on your OS
```

**Terminal 3 - Backend API**:
```bash
cd backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

**Terminal 4 - Celery Worker**:
```bash
cd backend
source venv/bin/activate
celery -A config worker -l info
```

**Terminal 5 - Frontend**:
```bash
cd frontend
npm run dev
```

---

## Useful Commands

### Backend

```bash
# Create new Django app
python manage.py startapp app_name

# Create migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
pytest

# Run with specific settings
python manage.py runserver --settings=config.settings.development
```

### Frontend

```bash
# Build for production
npm run build

# Run production build locally
npm run build && npm run start

# Run tests
npm test

# Linting
npm run lint

# Format code
npm run format
```

### Database

```bash
# Backup
pg_dump -U hackxharder -d hackxharder_db > backup.sql

# Restore
psql -U hackxharder -d hackxharder_db < backup.sql

# Connect to DB
psql -U hackxharder -d hackxharder_db -h localhost
```

---

## Troubleshooting

### PostgreSQL Connection Error
```
psycopg2.OperationalError: could not connect to server
```
**Solution**: Ensure PostgreSQL service is running.
```bash
# Ubuntu
sudo systemctl start postgresql

# macOS
brew services start postgresql@15
```

### Redis Connection Error
```
redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379
```
**Solution**: Start Redis.
```bash
# Docker
docker start hackxharder-redis

# Local
redis-server
```

### Port Already in Use
If `localhost:8000` or `localhost:3000` already in use:
```bash
# Backend (run on different port)
python manage.py runserver 0.0.0.0:8001

# Frontend (run on different port)
npm run dev -- --port 3001
```

### Database Migrations Conflict
```bash
# Reset database (careful! Deletes all data)
python manage.py migrate zero
python manage.py migrate

# Or drop database and recreate
dropdb -U postgres hackxharder_db
createdb -U postgres hackxharder_db
python manage.py migrate
```

### Celery Tasks Not Running
```bash
# Restart Celery worker
celery -A config worker -l info --purge
```

---

## Environment Variables Reference

| Variable | Example | Description |
|----------|---------|-------------|
| DEBUG | True | Enable debug mode (dev only) |
| SECRET_KEY | dev-key-... | Django secret key |
| DB_HOST | localhost | PostgreSQL host |
| DB_USER | hackxharder | PostgreSQL user |
| DB_PASSWORD | password | PostgreSQL password |
| DB_NAME | hackxharder_db | Database name |
| DB_PORT | 5432 | PostgreSQL port |
| REDIS_URL | redis://localhost:6379/0 | Redis URL |
| CORS_ALLOWED_ORIGINS | http://localhost:3000 | Frontend origin |
| EMAIL_BACKEND | console | Email backend (console for dev) |

---

## Next Steps

1. ✓ PostgreSQL running locally
2. ✓ Redis running (Docker or local)
3. ✓ Backend migrations applied
4. ✓ Frontend dependencies installed
5. Create sample data: `python manage.py seed_data` (when implemented)
6. Test API: Visit `http://localhost:8000/api/v1/docs/`
7. Start building features!
