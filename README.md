# HackXHarder

**Bug Bounty & Responsible Vulnerability Disclosure Platform**

Crowdsource security improvements. Researchers find vulnerabilities → Companies triage & reward → Bounties paid out.

---

## Quick Start

### 30-Second Setup

```bash
# 1. Start Redis (Docker)
docker-compose up -d redis

# 2. Backend (Terminal 1)
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# 3. Frontend (Terminal 2)
cd frontend
npm install
npm run dev
```

Backend: **http://localhost:8000**
Frontend: **http://localhost:3000**
API Docs: **http://localhost:8000/api/v1/docs/**

See **[QUICKSTART.md](QUICKSTART.md)** for full instructions.

---

## Project Structure

```
hackxharder/
├── backend/                 # Django REST API
│   ├── config/             # Settings, urls, wsgi, celery
│   ├── apps/               # 10 modular Django apps
│   │   ├── accounts/       # Auth, User, Profile, 2FA
│   │   ├── researchers/    # Researcher profiles
│   │   ├── companies/      # Companies & Programs
│   │   ├── reports/        # Vulnerability reports
│   │   ├── triage/         # Triage workflow
│   │   ├── messaging/      # In-app messaging
│   │   ├── payments/       # Bounty & payments
│   │   ├── admin_panel/    # Admin features
│   │   ├── audit/          # Logging & compliance
│   │   └── security/       # Encryption & RBAC
│   ├── requirements.txt    # Python dependencies
│   ├── manage.py           # Django CLI
│   └── .env.example        # Environment config
│
├── frontend/               # Next.js React SPA
│   ├── src/
│   │   ├── app/           # Pages
│   │   ├── components/    # Reusable UI
│   │   ├── services/      # API client
│   │   ├── store/         # Redux state
│   │   ├── hooks/         # Custom hooks
│   │   ├── types/         # TypeScript defs
│   │   └── styles/        # Global CSS
│   ├── package.json
│   └── .env.local.example
│
├── docs/                   # Documentation
│   ├── LOCAL_SETUP.md      # Local dev guide
│   ├── tasklist.md         # 400+ task checklist
│   ├── HackXHarder_Developer_Documentation.md  # Full spec
│   └── api.md              # API endpoints
│
├── docker-compose.yml      # Redis (optional)
├── QUICKSTART.md           # 30-second start
├── README.md               # This file
└── .git/                   # Version control
```

---

## Tech Stack

### Backend
- **Framework**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL 15 (dev: SQLite)
- **Cache/Queue**: Redis 7
- **Async**: Celery 5.3
- **Auth**: JWT (simplejwt) + 2FA (pyotp)
- **Encryption**: AES-256
- **API Docs**: drf-spectacular (Swagger/OpenAPI)

### Frontend
- **Framework**: Next.js 14 + React 18
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State**: Redux Toolkit
- **HTTP**: Axios
- **Forms**: React Hook Form + Zod

### Infrastructure
- **Web Server**: Nginx (reverse proxy)
- **App Server**: Gunicorn
- **Containerization**: Docker
- **Testing**: pytest, Jest

---

## Features (MVP)

### Researchers
- ✓ Browse active bug bounty & VDP programs
- ✓ Submit vulnerability reports with attachments
- ✓ Real-time status tracking (submitted → triaging → validated → resolved)
- ✓ Secure in-app messaging (encrypted)
- ✓ Earnings wallet + payment history
- ✓ Profile + reputation tracking

### Companies
- ✓ Create VDP or Bug Bounty programs
- ✓ Define scope (in-scope/out-of-scope domains)
- ✓ Configure severity levels & reward tiers
- ✓ Manage triage team
- ✓ Report queue + analytics

### Triage Team
- ✓ Report queue with filters
- ✓ Severity assessment (CVSS)
- ✓ Duplicate detection
- ✓ Internal notes (hidden from researchers)
- ✓ Researcher communication

### Platform Admin
- ✓ User management (suspend/restore)
- ✓ Audit logs (2-year retention)
- ✓ Dispute resolution
- ✓ System configuration
- ✓ Content moderation

---

## Development

### Setup

**Full guide**: See [docs/LOCAL_SETUP.md](docs/LOCAL_SETUP.md)

**Quick**:
```bash
# Prerequisites: Python 3.10+, Node 18+, PostgreSQL 15, Docker (optional)

# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Edit database config
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
npm install
cp .env.local.example .env.local
npm run dev

# Redis (Docker)
docker-compose up -d redis
```

### Environment Variables

**Backend** (`.env`):
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_HOST=localhost
DB_USER=hackxharder
DB_PASSWORD=password
DB_NAME=hackxharder_db
REDIS_URL=redis://localhost:6379/0
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

**Frontend** (`.env.local`):
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_ENVIRONMENT=development
```

### Common Commands

**Backend**:
```bash
cd backend
source venv/bin/activate

python manage.py migrate         # Run migrations
python manage.py createsuperuser # Create admin user
python manage.py runserver       # Start dev server
pytest                           # Run tests
celery -A config worker -l info  # Start background jobs
```

**Frontend**:
```bash
cd frontend
npm install                      # Install deps
npm run dev                      # Dev server
npm run build                    # Production build
npm test                         # Run tests
npm run lint                     # Code quality
```

### Database

PostgreSQL setup:
```bash
psql -U postgres

CREATE DATABASE hackxharder_db;
CREATE USER hackxharder WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE hackxharder_db TO hackxharder;
```

---

## API Documentation

Interactive API docs available at **http://localhost:8000/api/v1/docs/**

### Core Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/auth/register` | POST | Register new user |
| `/api/v1/auth/login` | POST | Login (returns JWT) |
| `/api/v1/auth/2fa/setup` | POST | Enable 2FA |
| `/api/v1/auth/profile` | GET/PUT | User profile |
| `/api/v1/programs` | GET/POST | Browse/create programs |
| `/api/v1/reports` | GET/POST | Submit/view reports |
| `/api/v1/triage/queue` | GET | Triage queue |
| `/api/v1/messages` | GET/POST | Messaging |
| `/api/v1/admin/users` | GET | User management |

Full list: [docs/api.md](docs/api.md)

---

## Project Roadmap

### Phase 1: MVP (✓ In Progress - Week 8)
- ✓ Auth system (register, login, 2FA, password reset)
- ✓ User & Profile models
- ✓ Project structure & settings
- In progress: Researcher + Company models
- Next: Reports, Triage, Messaging, Payments

### Phase 2: Beta (Weeks 9–12)
- Bounty & payment system
- Advanced duplicate detection
- Reputation scoring
- Bug fixes & refinement

### Phase 3: Production (Weeks 13+)
- S3 file storage
- Payment processor integration
- Third-party monitoring (Sentry, DataDog)
- Public launch

---

## Security

✓ **Authentication**: JWT + 2FA (TOTP)
✓ **Encryption**: AES-256 at rest (PII, messages, wallets)
✓ **API Security**: CSRF, XSS, SQL injection prevention
✓ **Rate Limiting**: Per-user + per-IP limits
✓ **Audit Logging**: All user actions logged (2-year retention)
✓ **RBAC**: 4 role-based access levels
✓ **File Uploads**: Type validation, ClamAV scan, quarantine

See [docs/HackXHarder_Developer_Documentation.md](docs/HackXHarder_Developer_Documentation.md) for full security spec.

---

## Testing

```bash
# Backend
cd backend
pytest                    # All tests
pytest --cov            # Coverage report
pytest -k test_auth     # Specific test

# Frontend
cd frontend
npm test                # Run Jest
npm run test:watch     # Watch mode
npm run test:coverage  # Coverage report
```

---

## Deployment

**Docker** (production):
```bash
docker-compose -f docker-compose.prod.yml up -d
```

**Manual** (VPS/cloud):
```bash
# Install deps
sudo apt install python3.10 postgresql redis-server nginx

# Clone + setup
git clone <repo>
cd hackxharder/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Migrations
python manage.py migrate

# Collect static
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

See [docs/LOCAL_SETUP.md](docs/LOCAL_SETUP.md) for full deployment guide.

---

## Contributing

1. Create feature branch: `git checkout -b feature/name`
2. Make changes + commit: `git commit -m "feat: description"`
3. No force push to main
4. Create PR with description
5. Code review required before merge

**Commit format**: Conventional Commits
- `feat:` New feature
- `fix:` Bug fix
- `chore:` Setup/tooling
- `docs:` Documentation
- `test:` Tests

---

## License

Proprietary. All rights reserved.

---

## Contact

**Developer**: Boni Yeamin  
**Email**: boni.ielts@gmail.com  
**GitHub**: [boni-yelts](https://github.com)

---

## Resources

- **Full Documentation**: [docs/HackXHarder_Developer_Documentation.md](docs/HackXHarder_Developer_Documentation.md)
- **API Spec**: [docs/api.md](docs/api.md)
- **Task Checklist**: [docs/tasklist.md](docs/tasklist.md)
- **Local Setup**: [docs/LOCAL_SETUP.md](docs/LOCAL_SETUP.md)
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)

---

**Status**: MVP in development (Sprint 1-2 complete)  
**Last Updated**: 2026-06-24  
**Version**: 0.1.0 (Alpha)
