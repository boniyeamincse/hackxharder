# HackXHarder - Complete Developer Documentation

## 1. Project Title
**HackXHarder** - A Bug Bounty and Responsible Vulnerability Disclosure Platform

---

## 2. Project Overview

HackXHarder is a comprehensive web-based platform that bridges the gap between ethical hackers, security researchers, organizations, and vulnerability management teams. The platform facilitates structured vulnerability reporting, triage, communication, and reward distribution in a secure, audited environment.

**Platform Purpose**: Enable organizations to crowdsource security improvements while protecting researcher identity, establishing clear scope boundaries, and ensuring vulnerability reports reach the right teams for rapid remediation.

---

## 3. Vision and Goal

**Vision**: To become the trusted platform for responsible vulnerability disclosure, making security research accessible, fair, and rewarding for researchers while reducing security blind spots for organizations.

**Goal**: Implement a scalable, secure MVP that:
- Eliminates barriers to ethical hacking participation
- Provides organizations with structured vulnerability intake and triage workflows
- Ensures researcher recognition and fair compensation
- Maintains audit trails for compliance and security monitoring
- Protects sensitive vulnerability data with encryption and access controls

---

## 4. Problem Statement

**Current Challenges**:
1. Organizations lack centralized, secure channels for receiving vulnerability reports
2. Researchers struggle to find legitimate bounty programs or responsible disclosure channels
3. Manual vulnerability triage processes are error-prone and slow
4. Researchers face identity theft risk and lack transparent reward clarity
5. Communication between researchers and companies often breaks down mid-disclosure
6. Organizations cannot track vulnerability lifecycle or maintain audit compliance
7. No standardized severity assessment or reward valuation

**HackXHarder Solution**: Unified platform with built-in triage workflows, researcher protection, transparent communication, and audit compliance.

---

## 5. Target Users

### 5.1 Researcher (Ethical Hacker / Security Researcher)
- **Profile**: Independent security researchers, bug bounty hunters, cybersecurity professionals
- **Pain Points**: 
  - Finding legitimate programs to test
  - Risk of identity exposure
  - Unclear payment terms and timelines
  - Confusion about scope and eligibility
- **Goals**:
  - Earn rewards for vulnerability findings
  - Maintain anonymity and privacy
  - Receive clear feedback on submission status
  - Access transparent reward history

### 5.2 Company (Program Owner)
- **Profile**: Startups to enterprises, SaaS companies, fintech platforms
- **Pain Points**:
  - No centralized vulnerability intake system
  - Difficulty managing incoming reports
  - Unclear responsibility for triage and response
  - Risk of duplicate reports and research
  - Scope creep and out-of-scope submissions
- **Goals**:
  - Define clear security program scope
  - Receive structured vulnerability reports
  - Assign reports to appropriate teams
  - Track resolution progress
  - Manage researcher relationships

### 5.3 Triage Team (Internal Security Team)
- **Profile**: Security engineers, security operations teams, incident response team members
- **Pain Points**:
  - Manual triage processes
  - Lack of standardized report formats
  - Difficulty assessing duplicate reports
  - Communication bottlenecks with researchers
  - No centralized log for compliance audits
- **Goals**:
  - Quickly assess report validity
  - Prioritize by severity and exploitability
  - Communicate status to researchers
  - Track remediation timeline
  - Generate security metrics and reports

### 5.4 Platform Admin (HackXHarder Team)
- **Profile**: Platform operators, support team, compliance officers
- **Pain Points**:
  - Managing multiple organizations and programs
  - Escalating disputes or payment issues
  - Monitoring platform health and abuse
  - Compliance and regulatory tracking
- **Goals**:
  - Monitor platform metrics
  - Manage user accounts and permissions
  - Handle escalations and disputes
  - View audit logs across organizations
  - Generate compliance reports

---

## 6. Core Features

### 6.1 Researcher Features

| Feature | Description | Priority |
|---------|-------------|----------|
| **Browse Programs** | Search and filter active bug bounty and VDP programs with scope visibility | MVP |
| **Submit Vulnerability Report** | Create detailed reports with attachments, PoC code, screenshots | MVP |
| **Real-time Status Tracking** | View submission workflow (Submitted → Triaging → Validated → Resolved) | MVP |
| **Researcher Dashboard** | View all submissions, earnings, reputation, communication timeline | MVP |
| **In-app Messaging** | Secure, encrypted communication with triage teams (no direct email exposure) | MVP |
| **Report History** | Permanent record of submissions with proof of disclosure date | MVP |
| **Earnings Wallet** | Track bounty earnings, payout status, payment method management | Post-MVP |
| **Reputation Score** | Build researcher credibility through validated findings | Post-MVP |
| **Program Notifications** | Alerts when new programs open, scope changes, reward updates | MVP |
| **Email Privacy** | Option to hide email; all communication through platform | MVP |

### 6.2 Company Features

| Feature | Description | Priority |
|---------|-------------|----------|
| **Create Security Program** | Launch VDP or bug bounty with custom branding, scope, rules | MVP |
| **Define Scope** | Specify in-scope/out-of-scope domains, API endpoints, services | MVP |
| **Program Settings** | Configure severity levels, reward tiers, disclosure policy | MVP |
| **Report Queue** | Centralized dashboard for incoming vulnerability reports | MVP |
| **Assign to Team** | Route reports to specific triage team members | MVP |
| **Severity Assessment Tool** | Standard templates for CVSS, severity classification | MVP |
| **Communication Panel** | Send secure messages to researchers, request clarification | MVP |
| **Report Status Workflow** | Move reports through triage → validation → fix → closure | MVP |
| **Duplicate Detection** | Flag potential duplicate reports for review | MVP |
| **Reward Management** | Set bounty amounts, track payouts, generate invoices | MVP |
| **Program Analytics** | Metrics on submissions, response times, costs, researcher activity | Post-MVP |
| **Custom Fields** | Add company-specific data fields to report forms | Post-MVP |
| **Automated Notifications** | Alerts for high-severity reports, researcher updates | MVP |
| **Report Export** | Compliance-ready exports (audit trail, CVE details) | MVP |

### 6.3 Triage Team Features

| Feature | Description | Priority |
|---------|-------------|----------|
| **Report Dashboard** | Filtered view of assigned reports with priority indicators | MVP |
| **Triage Workflow** | Mark reports as valid/invalid/duplicate with reasoning | MVP |
| **Severity Assessment** | Apply CVSS scores and internal severity ratings | MVP |
| **Duplicate Grouping** | Link duplicate reports, recognize first reporter | MVP |
| **Internal Notes** | Leave comments, technical notes (hidden from researcher) | MVP |
| **Progress Updates** | Send status messages to researcher at each workflow stage | MVP |
| **Attachment Review** | Securely view PoC code, screenshots, technical documentation | MVP |
| **Remediation Tracking** | Monitor fix progress, set estimated fix dates | MVP |
| **Communication History** | Full audit trail of all triage team communications | MVP |
| **Bulk Actions** | Batch update reports, reassign queues | Post-MVP |

### 6.4 Admin Features

| Feature | Description | Priority |
|---------|-------------|----------|
| **User Management** | Create, modify, suspend users and organizations | MVP |
| **Role Assignment** | Assign permissions (researcher, company admin, triage, platform admin) | MVP |
| **Organization Management** | Create and manage multiple organizations on platform | MVP |
| **Audit Dashboard** | View all actions across platform (authentication, data access, changes) | MVP |
| **Compliance Reporting** | Generate GDPR, SOC 2, regulatory compliance reports | Post-MVP |
| **Dispute Resolution** | Access interface for escalation and dispute handling | MVP |
| **Payment Management** | Review bounty payouts, manage payment methods | Post-MVP |
| **Content Moderation** | Flag and remove inappropriate content or spam reports | MVP |
| **System Health Monitoring** | Database performance, API latency, error rates | Post-MVP |
| **User Suspension/Termination** | Handle abuse, fraud, TOS violations | MVP |

---

## 7. Program Types

### 7.1 Vulnerability Disclosure Program (VDP)

**Definition**: Non-monetary, researcher-friendly program where companies welcome vulnerability reports but offer no cash reward.

**Use Cases**:
- Startups building security reputation
- Open-source projects
- Organizations committed to responsible disclosure but with limited budgets

**Default Configuration**:
- Scope: Clearly defined in-scope and out-of-scope
- Response SLA: Target response within 5-7 business days
- Reward: "Hall of fame" recognition (no bounty)
- Public: Can be listed publicly
- Disclosure Timeline: Agreed upon by both parties

### 7.2 Bug Bounty Program

**Definition**: Monetized program where researchers receive financial rewards for valid vulnerability findings.

**Use Cases**:
- Well-funded organizations
- High-security-criticality applications
- Organizations needing rapid vulnerability identification
- Enterprise security programs

**Default Configuration**:
- Scope: Clear boundaries with specific in-scope components
- Response SLA: Target response within 24-48 hours
- Reward Tiers: Tiered by severity (critical, high, medium, low)
- Public: Listed with reward amounts visible
- Disclosure Timeline: Legal disclosure agreement required
- Payment Method: Direct transfer, crypto, or third-party processor

---

## 8. MVP Scope

### 8.1 In Scope (MVP Phase 1)

**Core Workflows**:
- ✓ Researcher registration and profile management
- ✓ Company onboarding and program creation
- ✓ Program scope definition (domain/API list)
- ✓ Vulnerability report submission with attachments
- ✓ Automated report intake validation
- ✓ Triage team assignment and workflow
- ✓ Report status tracking (5-stage lifecycle)
- ✓ CVSS severity classification
- ✓ In-app secure messaging (no email exposure)
- ✓ Researcher payment wallet setup
- ✓ Basic platform admin dashboard
- ✓ Audit logging for all user actions
- ✓ 2FA authentication for all user types
- ✓ Role-based access control (4 roles)

**Security Baseline**:
- ✓ Data encryption at rest (PII, vulnerability reports)
- ✓ HTTPS/TLS for all communications
- ✓ CSRF and XSS protection
- ✓ Rate limiting on all public endpoints
- ✓ Secure file upload (virus scanning, isolation)
- ✓ Content Security Policy (CSP) headers
- ✓ SQL injection prevention (parameterized queries)
- ✓ Session management and timeout

**Infrastructure**:
- ✓ Local file storage for MVP (transition to S3 in production)
- ✓ Docker containerization
- ✓ Nginx reverse proxy
- ✓ Gunicorn WSGI server
- ✓ PostgreSQL database
- ✓ Redis for background job queues

### 8.2 Out of Scope (Post-MVP)

**Features for Future Phases**:
- Automated vulnerability disclosure timeline enforcement
- CVE publication and vulnerability database integration
- Advanced analytics and trend reporting
- Researcher reputation/leaderboard system
- Multi-currency and international payment methods
- Custom report templates per organization
- API for third-party integrations
- Mobile application
- Automated remediation suggestions (ML-based)
- Integration with vulnerability management platforms (Jira, Slack, etc.)

---

## 9. Future Scope (Post-MVP Roadmap)

### Phase 2: Enhanced Triage & Communication
- Advanced duplicate detection (heuristic + ML)
- Automated severity scoring recommendations
- Email notification templates
- Researcher feedback surveys

### Phase 3: Analytics & Insights
- Organization security metrics dashboard
- Vulnerability trends per industry
- Researcher leaderboards and recognition
- CVSS distribution visualization

### Phase 4: Integrations & Automation
- Slack/Teams integration for triage notifications
- Jira integration for ticket creation
- Custom webhook system
- REST API for third-party tools

### Phase 5: Advanced Security
- Fuzzing and automated testing tools for researchers
- Proof-of-concept sandbox environment
- Advanced encryption and key management
- SOC 2 Type II compliance

---

## 10. User Roles and Permissions

### 10.1 Role Hierarchy and Permissions

| Permission | Researcher | Company Admin | Triage Lead | Platform Admin |
|-----------|-----------|--------------|------------|----------------|
| Browse programs | ✓ | - | - | ✓ |
| Submit reports | ✓ | - | - | - |
| Create program | - | ✓ | - | ✓ |
| Manage program settings | - | ✓ | - | ✓ |
| Access triage queue | - | - | ✓ | ✓ |
| Assign reports | - | - | ✓ | ✓ |
| Validate/reject reports | - | - | ✓ | ✓ |
| Send researcher messages | - | - | ✓ | ✓ |
| Manage users | - | - | - | ✓ |
| View audit logs | - | - | - | ✓ |
| Suspend accounts | - | - | - | ✓ |
| Process payments | - | - | - | ✓ |
| Edit own profile | ✓ | ✓ | ✓ | ✓ |
| Enable 2FA | ✓ | ✓ | ✓ | ✓ |

### 10.2 Permission Implementation

**Framework**: RBAC (Role-Based Access Control)
- Roles assigned at account creation
- Company Admins can assign Triage roles to team members
- Platform Admins manage all roles
- Permissions checked at API and view layer
- Audit log records all permission-based actions

---

## 11. Main Modules

### 11.1 Module Architecture Overview

```
HackXHarder Platform
├── Authentication & Authorization Module
├── Researcher Module
├── Company Module
├── Triage Module
├── Report Management Module
├── Messaging Module
├── Payment Module
├── Admin Module
├── Audit & Logging Module
└── Security & Compliance Module
```

### 11.2 Module Descriptions

| Module | Responsibility | Key Services |
|--------|-----------------|---------------|
| **Auth** | User registration, login, 2FA, session management | JWT tokens, OAuth integrations |
| **Researcher** | Researcher profiles, credentials, earnings tracking | Profile management, reputation |
| **Company** | Organization management, program creation, settings | Program CRUD, team management |
| **Triage** | Report queue management, workflow progression | Queue filtering, status updates |
| **Report** | Report submission, validation, storage, retrieval | Attachment handling, versioning |
| **Messaging** | Secure in-app communication between researchers and teams | Encrypted messages, notification delivery |
| **Payment** | Bounty management, payment processing, wallet tracking | Bounty calculation, payout scheduling |
| **Admin** | Platform administration, user management, compliance | User CRUD, audit reports |
| **Audit** | Comprehensive logging, action tracking, compliance reporting | Audit trail storage, log search |
| **Security** | Encryption, file upload handling, rate limiting | Cryptography, file scanning |

---

## 12. Suggested System Architecture

### 12.1 High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                          Client Layer                            │
├────────────────────┬────────────────────┬───────────────────────┤
│  Web Browser       │  Mobile (Future)   │  Admin Dashboard      │
│  (Next.js SPA)     │  (React Native)    │  (Next.js)            │
└────────┬───────────┴────────┬───────────┴──────────┬────────────┘
         │                    │                      │
         └────────────────────┼──────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │   Nginx Proxy      │
                    │  (SSL Termination) │
                    │  (Rate Limiting)   │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
    ┌────▼─────┐      ┌──────▼──────┐      ┌─────▼──────┐
    │ Gunicorn │      │  Gunicorn   │      │  Gunicorn  │
    │ Worker 1 │      │  Worker 2   │      │  Worker N  │
    │ (Django) │      │  (Django)   │      │  (Django)  │
    └────┬─────┘      └──────┬──────┘      └─────┬──────┘
         │                   │                    │
         └───────────────────┼────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────────┐    ┌─────▼──────┐    ┌─────▼──────┐
    │ PostgreSQL  │    │    Redis   │    │   File     │
    │  Database   │    │    Cache   │    │  Storage   │
    │             │    │ Job Queue  │    │   (Local)  │
    └─────────────┘    └────────────┘    └────────────┘
         │                    │
         │                ┌───▼────────┐
         │                │   Celery   │
         │                │  Workers   │
         │                └────────────┘
         │
    ┌────▼──────────────────────────┐
    │   Backup & Audit Logs          │
    │   (PostgreSQL, S3 future)      │
    └───────────────────────────────┘
```

### 12.2 Technology Stack Detail

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js + React | SPA for web interface |
| **Backend** | Django REST Framework | RESTful API service |
| **Database** | PostgreSQL | Relational data storage |
| **Cache/Queue** | Redis | Caching and job queueing |
| **Job Worker** | Celery | Async task processing |
| **Web Server** | Nginx | Reverse proxy, SSL |
| **App Server** | Gunicorn | WSGI server for Django |
| **Containerization** | Docker | Development and deployment |
| **File Storage** | Local (MVP), S3 (Prod) | Attachment and document storage |

---

## 13. Backend Architecture

### 13.1 Django Project Structure

```
backend/
├── manage.py
├── requirements.txt
├── Dockerfile
├── .env.example
│
├── config/
│   ├── settings/
│   │   ├── base.py          (Common settings)
│   │   ├── development.py   (Dev-specific)
│   │   ├── production.py    (Prod-specific)
│   │   └── testing.py       (Test-specific)
│   ├── urls.py              (URL routing)
│   ├── wsgi.py              (WSGI entry)
│   └── celery.py            (Celery config)
│
├── apps/
│   ├── accounts/            (Auth & user management)
│   │   ├── models.py        (User, Profile models)
│   │   ├── views.py         (Auth endpoints)
│   │   ├── serializers.py   (Data serialization)
│   │   ├── permissions.py   (RBAC logic)
│   │   └── tests.py
│   │
│   ├── researchers/         (Researcher-specific logic)
│   │   ├── models.py        (Researcher, Credentials)
│   │   ├── views.py         (Researcher endpoints)
│   │   ├── serializers.py
│   │   └── tests.py
│   │
│   ├── companies/           (Company & program management)
│   │   ├── models.py        (Company, Program, Scope)
│   │   ├── views.py         (Program CRUD endpoints)
│   │   ├── serializers.py
│   │   └── tests.py
│   │
│   ├── reports/             (Vulnerability report system)
│   │   ├── models.py        (Report, Attachment, Comment)
│   │   ├── views.py         (Report submission/retrieval)
│   │   ├── serializers.py
│   │   ├── tasks.py         (Celery tasks for report processing)
│   │   ├── validators.py    (Report validation logic)
│   │   └── tests.py
│   │
│   ├── triage/              (Triage workflow)
│   │   ├── models.py        (TriageAssignment, StatusHistory)
│   │   ├── views.py         (Triage queue endpoints)
│   │   ├── serializers.py
│   │   ├── services.py      (Duplicate detection, workflow logic)
│   │   └── tests.py
│   │
│   ├── messaging/           (In-app communication)
│   │   ├── models.py        (Message, Conversation)
│   │   ├── views.py         (Messaging endpoints)
│   │   ├── serializers.py
│   │   ├── tasks.py         (Email notification tasks)
│   │   └── tests.py
│   │
│   ├── payments/            (Bounty & payment tracking)
│   │   ├── models.py        (Bounty, Payout, Wallet)
│   │   ├── views.py         (Payment endpoints)
│   │   ├── serializers.py
│   │   ├── tasks.py         (Payout processing)
│   │   └── tests.py
│   │
│   ├── admin_panel/         (Platform administration)
│   │   ├── models.py        (AdminAction, Dispute)
│   │   ├── views.py         (Admin endpoints)
│   │   ├── serializers.py
│   │   └── tests.py
│   │
│   ├── audit/               (Logging & compliance)
│   │   ├── models.py        (AuditLog, AuditTrail)
│   │   ├── middleware.py    (Request/response logging)
│   │   ├── utils.py         (Logging helpers)
│   │   └── tests.py
│   │
│   └── security/            (Encryption & file handling)
│       ├── encryption.py    (AES-256 encryption utils)
│       ├── file_handler.py  (Secure upload/download)
│       ├── permissions.py   (RBAC decorators)
│       └── validators.py    (Input validation)
│
├── utils/
│   ├── decorators.py        (Rate limiting, logging decorators)
│   ├── exceptions.py        (Custom exceptions)
│   ├── helpers.py           (General utilities)
│   └── constants.py         (App-wide constants)
│
├── tests/
│   ├── fixtures/            (Test data)
│   ├── integration/         (Integration tests)
│   └── conftest.py          (Pytest configuration)
│
└── logs/
    └── application.log      (Runtime logs)
```

### 13.2 API Endpoint Groups

```
Authentication & Authorization
  POST   /api/v1/auth/register
  POST   /api/v1/auth/login
  POST   /api/v1/auth/logout
  POST   /api/v1/auth/refresh-token
  POST   /api/v1/auth/2fa/setup
  POST   /api/v1/auth/2fa/verify
  POST   /api/v1/auth/password-reset

Researcher Endpoints
  GET    /api/v1/researchers/profile
  PUT    /api/v1/researchers/profile
  GET    /api/v1/researchers/programs
  GET    /api/v1/researchers/reports
  GET    /api/v1/researchers/earnings
  GET    /api/v1/researchers/wallet

Company/Program Endpoints
  POST   /api/v1/programs
  GET    /api/v1/programs
  GET    /api/v1/programs/{id}
  PUT    /api/v1/programs/{id}
  DELETE /api/v1/programs/{id}
  POST   /api/v1/programs/{id}/scope
  GET    /api/v1/programs/{id}/team
  POST   /api/v1/programs/{id}/team/invite

Report Management Endpoints
  POST   /api/v1/reports
  GET    /api/v1/reports/{id}
  PUT    /api/v1/reports/{id}
  GET    /api/v1/reports/{id}/comments
  POST   /api/v1/reports/{id}/comments
  POST   /api/v1/reports/{id}/attachments
  GET    /api/v1/reports/{id}/attachments/{file-id}

Triage Endpoints
  GET    /api/v1/triage/queue
  PUT    /api/v1/triage/reports/{id}/status
  POST   /api/v1/triage/reports/{id}/severity
  PUT    /api/v1/triage/reports/{id}/assign
  POST   /api/v1/triage/reports/{id}/notes

Messaging Endpoints
  GET    /api/v1/messages
  POST   /api/v1/messages
  GET    /api/v1/conversations/{id}
  POST   /api/v1/conversations/{id}/messages

Payment Endpoints
  GET    /api/v1/payments/wallet
  GET    /api/v1/payments/history
  POST   /api/v1/payments/method
  GET    /api/v1/payments/bounties/{program-id}

Admin Endpoints
  GET    /api/v1/admin/users
  POST   /api/v1/admin/users/{id}/suspend
  GET    /api/v1/admin/audit-logs
  GET    /api/v1/admin/reports
  POST   /api/v1/admin/disputes/{id}/resolve
```

### 13.3 Key Django Components

**Middleware Stack**:
- CORS handling
- Request/response logging (audit trail)
- Rate limiting
- Authentication verification
- Permission checks

**Custom Decorators**:
- `@require_role(...)` - Role-based access control
- `@audit_log` - Log user actions
- `@rate_limit(...)` - Rate limit by user/IP
- `@encrypt_response` - Encrypt sensitive data

**Signals** (Django signals for async workflows):
- `post_save` on Report → trigger validation task
- `post_save` on TriageAssignment → notify researcher
- `post_save` on ReportStatus → log to audit trail

---

## 14. Frontend Architecture

### 14.1 Next.js Project Structure

```
frontend/
├── package.json
├── next.config.js
├── tsconfig.json
├── .env.local.example
│
├── public/              (Static assets)
│   ├── logo.svg
│   ├── favicons/
│   └── assets/
│
├── src/
│   ├── app/             (Next.js app directory)
│   │   ├── layout.tsx   (Root layout)
│   │   ├── page.tsx     (Home page)
│   │   │
│   │   ├── auth/        (Authentication pages)
│   │   │   ├── login/page.tsx
│   │   │   ├── register/page.tsx
│   │   │   ├── 2fa/page.tsx
│   │   │   └── password-reset/page.tsx
│   │   │
│   │   ├── dashboard/   (User dashboards)
│   │   │   ├── researcher/page.tsx
│   │   │   ├── company/page.tsx
│   │   │   ├── triage/page.tsx
│   │   │   └── admin/page.tsx
│   │   │
│   │   ├── programs/    (Program browsing)
│   │   │   ├── page.tsx (Program list)
│   │   │   ├── [id]/page.tsx (Program details)
│   │   │   └── [id]/submit/page.tsx (Report submission)
│   │   │
│   │   ├── reports/     (Report management)
│   │   │   ├── [id]/page.tsx (Report detail)
│   │   │   └── [id]/edit/page.tsx
│   │   │
│   │   ├── messages/    (Messaging)
│   │   │   ├── page.tsx (Inbox)
│   │   │   └── [id]/page.tsx (Conversation)
│   │   │
│   │   └── admin/       (Admin panel)
│   │       ├── users/page.tsx
│   │       ├── audit/page.tsx
│   │       └── disputes/page.tsx
│   │
│   ├── components/      (Reusable UI components)
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   ├── RegisterForm.tsx
│   │   │   └── TwoFactorSetup.tsx
│   │   │
│   │   ├── layout/
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── Navbar.tsx
│   │   │
│   │   ├── forms/
│   │   │   ├── ReportSubmissionForm.tsx
│   │   │   ├── ProgramCreationForm.tsx
│   │   │   └── TriageForm.tsx
│   │   │
│   │   ├── reports/
│   │   │   ├── ReportCard.tsx
│   │   │   ├── ReportList.tsx
│   │   │   ├── ReportDetail.tsx
│   │   │   └── AttachmentUploader.tsx
│   │   │
│   │   ├── triage/
│   │   │   ├── TriageQueue.tsx
│   │   │   ├── ReportTriage.tsx
│   │   │   └── SeveritySelector.tsx
│   │   │
│   │   ├── messaging/
│   │   │   ├── MessageList.tsx
│   │   │   ├── MessageComposer.tsx
│   │   │   └── ConversationList.tsx
│   │   │
│   │   └── common/
│   │       ├── Button.tsx
│   │       ├── Modal.tsx
│   │       ├── Alert.tsx
│   │       ├── Spinner.tsx
│   │       ├── Table.tsx
│   │       └── Badge.tsx
│   │
│   ├── hooks/           (Custom React hooks)
│   │   ├── useAuth.ts
│   │   ├── useApi.ts
│   │   ├── usePagination.ts
│   │   ├── useLocalStorage.ts
│   │   └── useWindowSize.ts
│   │
│   ├── services/        (API client & business logic)
│   │   ├── api/
│   │   │   ├── client.ts (Axios instance)
│   │   │   ├── auth.ts
│   │   │   ├── reports.ts
│   │   │   ├── programs.ts
│   │   │   ├── triage.ts
│   │   │   ├── messages.ts
│   │   │   └── payments.ts
│   │   │
│   │   └── utils/
│   │       ├── validators.ts
│   │       ├── formatters.ts
│   │       └── constants.ts
│   │
│   ├── store/           (State management - Redux Toolkit)
│   │   ├── store.ts
│   │   ├── slices/
│   │   │   ├── authSlice.ts
│   │   │   ├── userSlice.ts
│   │   │   ├── reportSlice.ts
│   │   │   └── uiSlice.ts
│   │   │
│   │   └── hooks.ts (TypeScript hooks for Redux)
│   │
│   ├── types/           (TypeScript types)
│   │   ├── index.ts
│   │   ├── api.ts
│   │   ├── models.ts
│   │   └── enums.ts
│   │
│   ├── styles/          (Global styles)
│   │   ├── globals.css
│   │   ├── tailwind.config.js
│   │   └── variables.css
│   │
│   └── middleware.ts    (Next.js middleware - auth checks)
│
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

### 14.2 Frontend Technology Stack

| Purpose | Technology |
|---------|-----------|
| Framework | Next.js 14+ (App Router) |
| UI Library | React 18+ |
| Language | TypeScript |
| Styling | Tailwind CSS |
| Component Library | shadcn/ui or Headless UI |
| State Management | Redux Toolkit |
| HTTP Client | Axios + Interceptors |
| Form Handling | React Hook Form |
| Validation | Zod |
| Testing | Jest + React Testing Library |
| E2E Testing | Playwright or Cypress |
| Package Manager | npm or pnpm |

### 14.3 Frontend Features by Role

**Researcher Dashboard**:
- Program discovery and filtering
- Submit vulnerability report form
- Report status timeline
- Earnings dashboard
- Message inbox
- Profile and payment method management

**Company Admin Dashboard**:
- Program creation and management
- Scope definition interface
- Team member invitation
- Reward tier configuration
- Program analytics overview
- Payment history

**Triage Team Dashboard**:
- Report queue with filters (severity, status, assigned)
- Report detail view with full history
- Triage workflow (status update, severity assessment)
- Internal notes editor
- Researcher communication panel
- Duplicate report linking

**Admin Dashboard**:
- User management (search, suspend, roles)
- Audit log viewer with filtering
- Dispute resolution interface
- Platform metrics and health overview
- Organization management

---

## 15. Database Design Overview

### 15.1 Database Relationships Diagram (Entity Model)

```
User (auth_user)
├── Profile (accounts_profile)
├── Researcher (researchers_researcher)
├── Company (companies_company)
│   ├── Program (companies_program)
│   │   ├── Scope (companies_scope)
│   │   ├── SeverityLevel (companies_severitylevel)
│   │   ├── RewardTier (payments_rewardtier)
│   │   └── Report (reports_report)
│   │       ├── Attachment (reports_attachment)
│   │       ├── Comment (reports_comment)
│   │       ├── TriageAssignment (triage_triageassignment)
│   │       ├── StatusHistory (triage_statushistory)
│   │       └── Bounty (payments_bounty)
│   │
│   └── Team (companies_team)
│       └── TeamMember (companies_teammember) → User
│
├── Conversation (messaging_conversation)
│   └── Message (messaging_message)
│
├── Wallet (payments_wallet)
├── PaymentMethod (payments_paymentmethod)
├── Payout (payments_payout)
│
└── AuditLog (audit_auditlog)
```

### 15.2 Important Database Models

#### **User (accounts_user)**
- Extended Django User model
- Email, username, password hash
- is_active, is_staff, is_superuser
- date_joined, last_login

#### **Profile (accounts_profile)**
- Foreign Key: User (One-to-One)
- Role: RESEARCHER | COMPANY_ADMIN | TRIAGE_LEAD | ADMIN (enum)
- Avatar URL, bio, location
- two_fa_enabled, phone_number
- created_at, updated_at

#### **Researcher (researchers_researcher)**
- Foreign Key: User (One-to-One)
- reputation_score, verified (boolean)
- total_submissions, accepted_reports
- average_response_rating
- created_at

#### **Company (companies_company)**
- Foreign Key: User (Owner/Admin)
- Name, website, logo, description
- Industry, size (enum: startup, scaleup, enterprise)
- Subscription tier: FREE | PRO | ENTERPRISE
- created_at, updated_at

#### **Program (companies_program)**
- Foreign Key: Company
- Name, description, rules
- Type: VDP | BUG_BOUNTY (enum)
- Status: DRAFT | ACTIVE | PAUSED | CLOSED (enum)
- Scope: JSONB field with in-scope/out-of-scope domains
- Disclosure policy text
- created_at, updated_at, published_date

#### **Scope (companies_scope)**
- Foreign Key: Program
- Domain/API endpoint, scope_type: IN_SCOPE | OUT_OF_SCOPE
- Description, examples
- created_at

#### **Report (reports_report)**
- Foreign Key: Researcher, Program
- Title, description, vulnerability_details
- Attached files (store as JSON references to attachment IDs)
- Status: SUBMITTED | TRIAGING | VALIDATED | REJECTED | RESOLVED | DUPLICATE (enum)
- Severity: CRITICAL | HIGH | MEDIUM | LOW | INFO (enum) - nullable until triage
- cvss_score (float, 0-10)
- Unique constraint: (researcher_id, program_id, vulnerability_hash) for duplicate prevention
- created_at, updated_at

#### **Attachment (reports_attachment)**
- Foreign Key: Report
- File name, mime type, file size
- file_path (encrypted reference)
- uploaded_by (Researcher FK)
- scan_status: PENDING | SAFE | QUARANTINED (enum)
- created_at

#### **Comment (reports_comment)**
- Foreign Key: Report, User
- Comment text
- is_internal (boolean) - hidden from researchers if true
- created_at, updated_at

#### **TriageAssignment (triage_triageassignment)**
- Foreign Key: Report, User (triage team member)
- Priority: LOW | MEDIUM | HIGH | CRITICAL (enum)
- notes (internal)
- assigned_at, due_date
- created_at, updated_at

#### **StatusHistory (triage_statushistory)**
- Foreign Key: Report
- Old_status, new_status
- Changed_by (User FK)
- Changed_reason (comment)
- created_at

#### **Bounty (payments_bounty)**
- Foreign Key: Report, Program
- Amount (decimal)
- Currency (enum: USD, EUR, BTC, etc.)
- Status: PENDING | APPROVED | PAID | REJECTED (enum)
- Approved_by (User FK - triage team)
- Approved_date, paid_date
- created_at

#### **Wallet (payments_wallet)**
- Foreign Key: Researcher
- Balance (decimal, encrypted)
- Currency
- Last_updated, created_at

#### **PaymentMethod (payments_paymentmethod)**
- Foreign Key: Researcher
- Type: BANK_TRANSFER | CRYPTO | PAYPAL (enum)
- Details (encrypted)
- Verified (boolean)
- created_at

#### **Payout (payments_payout)**
- Foreign Key: Wallet, PaymentMethod
- Amount, currency
- Status: PENDING | PROCESSING | COMPLETED | FAILED (enum)
- Transaction_id (external reference)
- created_at, processed_at

#### **Message (messaging_message)**
- Foreign Key: Conversation, Sender (User)
- Content (encrypted)
- Read_by (ManyToMany with users)
- created_at, updated_at

#### **Conversation (messaging_conversation)**
- Foreign Key: Report
- Participants (ManyToMany: Researcher + Triage team members)
- Subject
- created_at, updated_at

#### **AuditLog (audit_auditlog)**
- User FK (nullable - for system actions)
- Action type: LOGIN | LOGOUT | CREATE | UPDATE | DELETE | DOWNLOAD (enum)
- Content type (model being modified)
- Object_id (id of modified object)
- Changes (JSONField - before/after values)
- IP address
- User agent
- Status: SUCCESS | FAILURE (enum)
- created_at

---

## 16. Vulnerability Report Workflow

### 16.1 Complete Report Lifecycle

```
SUBMITTED
    ↓
    [Automated Validation]
    ├─ Valid? ─→ TRIAGING
    │           ↓
    │           [Triage Team Assigns]
    │           ↓
    │           [Team Assesses Report]
    │           ↓
    │           Is Duplicate? ─→ DUPLICATE
    │           │
    │           No ─→ Valid Finding? 
    │               ├─ YES ─→ VALIDATED
    │               │         ↓
    │               │         [Bounty Calculated]
    │               │         ↓
    │               │         Approved for Reward?
    │               │         ├─ YES ─→ RESOLVED
    │               │         │         ↓
    │               │         │         [Bounty Paid]
    │               │         │         ↓
    │               │         │         CLOSED
    │               │         │
    │               │         └─ NO ─→ REJECTED
    │               │                  ↓
    │               │                  [Researcher Notified]
    │               │                  ↓
    │               │                  CLOSED
    │               │
    │               └─ NO ─→ REJECTED
    │                       ↓
    │                       CLOSED
    │
    └─ Invalid? ─→ REJECTED
                    ↓
                    CLOSED
```

### 16.2 Workflow Actions by Role

| Status | Researcher Action | Triage Action | Notes |
|--------|------------------|----------------|-------|
| SUBMITTED | View submission, add comments | Review quality, request clarification | Auto-validation runs |
| TRIAGING | Monitor progress, respond to questions | Assess validity, check duplicates | Max 48-hour SLA |
| VALIDATED | Monitor fix status | Calculate bounty, approve reward | High confidence finding |
| DUPLICATE | Notified of original report | Link to primary report | Researcher still credited |
| REJECTED | Request clarification via appeal | Explain rejection reason | Out-of-scope or invalid |
| RESOLVED | Receive bounty notification | Process payment | Vulnerability fixed |
| CLOSED | Download report receipt | Archive | Final state |

### 16.3 Report Status Definitions

| Status | Definition | Researcher Visibility |
|--------|-----------|----------------------|
| **SUBMITTED** | Report received and queued for triage | Full visibility |
| **TRIAGING** | Triage team actively reviewing | Full visibility + triage notes if added |
| **VALIDATED** | Report confirmed as genuine vulnerability | Full visibility, bounty amount disclosed |
| **DUPLICATE** | Vulnerability already reported | Notified, linked to primary report |
| **REJECTED** | Invalid, out-of-scope, or insufficient detail | Full visibility with rejection reason |
| **RESOLVED** | Vulnerability fixed by company | Full visibility, bounty paid |
| **CLOSED** | Report archived, no further action | Read-only visibility |

---

## 17. Severity Levels

### 17.1 CVSS-Based Severity Classification

| Severity | CVSS Score | Impact | Examples |
|----------|-----------|--------|----------|
| **CRITICAL** | 9.0-10.0 | Complete system compromise, data exfiltration | RCE, authentication bypass, SQL injection |
| **HIGH** | 7.0-8.9 | Significant impact, partial system compromise | XSS, CSRF, privilege escalation |
| **MEDIUM** | 4.0-6.9 | Moderate impact, some user data at risk | Path traversal, weak encryption, info disclosure |
| **LOW** | 0.1-3.9 | Minor impact, limited scope | Typos in error messages, deprecated SSL, low-risk config |
| **INFO** | 0.0 | Informational, no exploit | Best practice recommendations, outdated libraries |

### 17.2 Severity Assessment Process

1. **Automated Initial Assessment**:
   - Check report against known vulnerability patterns
   - Preliminary severity suggestion based on vulnerability type
   - Flag for manual review if uncertain

2. **Manual Triage Assessment**:
   - Triage team reviews automated suggestion
   - Applies CVSS v3.1 methodology if needed
   - Considers business context and exploitability
   - Documents reasoning in internal notes

3. **Final Severity Decision**:
   - Team lead approves/adjusts severity
   - Severity set in report record
   - Researcher notified of final severity
   - Bounty tier determined by severity and program rules

---

## 18. Reward/Bounty Management

### 18.1 Bounty Workflow

```
Report Validated
       ↓
Triage Team Determines Severity
       ↓
Bounty Tier Lookup (Program Scope)
       ├─ CRITICAL: $5,000 - $50,000
       ├─ HIGH:     $2,000 - $10,000
       ├─ MEDIUM:   $500  - $5,000
       └─ LOW:      $100  - $1,000
       ↓
Manager Approves Bounty Amount
       ↓
Bounty Created (PENDING Status)
       ↓
Researcher Notified via Message + Email
       ↓
Researcher Provides Payment Details
       ↓
Admin Processes Payout
       ├─ Bank Transfer (standard)
       ├─ Cryptocurrency
       └─ PayPal/Other
       ↓
Payout Status: COMPLETED
       ↓
Report Status: RESOLVED → CLOSED
```

### 18.2 Bounty Configuration Per Program

| Setting | Description | Customizable |
|---------|-------------|--------------|
| **Bounty Range** | Min/max for each severity tier | ✓ |
| **Payment Methods** | Accepted payment types | ✓ |
| **Processing Time** | Target payout timeline | ✓ |
| **Currency** | Primary payout currency | ✓ |
| **Duplicate Handling** | First reporter vs. all reporters | ✓ |
| **Approval Process** | Manual or automatic bounty approval | ✓ |
| **Tax Handling** | Company responsibility or deduction | ✓ |

### 18.3 Duplicate Report Handling

**Option 1**: Award bounty to first reporter only
- All duplicate reports linked to primary
- Other researchers notified they've been duplicated
- Encourages speed in reporting

**Option 2**: Award reduced bounty to all valid reports
- First reporter: 100% bounty
- Second reporter: 50% bounty
- Third+ reporter: 25% bounty
- Ensures researchers are rewarded for independent discovery

---

## 19. Notification System

### 19.1 Notification Channels

| Channel | Use Case | Recipient |
|---------|----------|-----------|
| **In-App Alert** | Immediate notification | All users |
| **Email** | Status updates, bounty notification | Researchers |
| **Push Notification** | Important updates (future) | Mobile users |
| **Webhook** | Company integrations (future) | External systems |

### 19.2 Notification Events

| Event | Trigger | Recipient | Channel |
|-------|---------|-----------|---------|
| **Report Submitted** | Researcher submits report | Triage team | In-app + Email |
| **Report Status Change** | Status progresses | Researcher | In-app + Email |
| **New Message** | Team sends message | Researcher | In-app + Email |
| **Bounty Approved** | Manager approves reward | Researcher | In-app + Email |
| **Payout Processed** | Payment transfers | Researcher | In-app + Email |
| **Duplicate Detected** | Report marked duplicate | Researcher | In-app + Email |
| **Triage Delay** | SLA approaching | Triage team | In-app Alert |

### 19.3 Notification Preferences

Users can configure:
- Notification frequency (immediate, daily digest, weekly digest)
- Notification channels (email on/off, push on/off)
- Critical alerts only (opt-in)
- Quiet hours (9pm-9am, no notifications)

---

## 20. File Upload and Attachment Handling

### 20.1 Upload Security Requirements

| Requirement | Implementation |
|------------|-----------------|
| **File Type Validation** | Whitelist: PDF, PNG, JPG, GIF, TXT, ZIP, RAR; Block executables |
| **File Size Limit** | Max 100MB per file, 500MB per report |
| **Virus Scanning** | ClamAV on upload (dev: placeholder, prod: real scan) |
| **Filename Sanitization** | Remove path traversal characters, store as UUID |
| **Secure Storage** | Local encrypted directory (dev) → S3 with encryption (prod) |
| **Access Control** | Only report owner + assigned triage team can download |
| **Encrypted URLs** | Time-limited signed download URLs with encryption |

### 20.2 Upload Workflow

```
User Selects File
       ↓
Frontend Validates:
├─ File type
├─ File size
└─ Mime type
       ↓
Upload to Server
       ↓
Backend Validates:
├─ MIME type again
├─ File size
└─ Magic bytes
       ↓
Virus Scan (ClamAV)
       ├─ SAFE ─→ Store encrypted
       │
       └─ DETECTED ─→ QUARANTINE + Notify admin
       ↓
Create Attachment Record
└─ Store encrypted file reference
       ↓
Return Attachment ID to Frontend
```

### 20.3 File Storage Implementation

**Development**:
```
/backend/media/
├── attachments/
│   ├── [uuid].pdf (encrypted)
│   ├── [uuid].png (encrypted)
│   └── ...
└── audit_exports/
    └── [uuid].csv (encrypted)
```

**Production** (Future):
- S3 bucket with KMS encryption
- CloudFront CDN for download distribution
- Lifecycle policies to archive old attachments after 1 year

---

## 21. Security Requirements

### 21.1 Authentication & Authorization

| Requirement | Implementation |
|------------|-----------------|
| **Password Strength** | Minimum 12 characters, complexity rules enforced |
| **Password Hashing** | PBKDF2 with Django default settings |
| **Two-Factor Authentication** | TOTP (Google Authenticator, Authy) mandatory for all users |
| **Session Management** | JWT tokens (access 15min, refresh 7 days) |
| **Password Reset** | Email verification link with 24-hour expiry |
| **Account Lockout** | Lock after 5 failed login attempts for 15 minutes |
| **Rate Limiting** | 10 attempts per minute per IP for login endpoint |

### 21.2 Data Encryption

| Data Type | Encryption | At Rest | In Transit |
|-----------|-----------|---------|-----------|
| **Passwords** | PBKDF2 | ✓ (hashed) | N/A |
| **2FA Secrets** | AES-256 | ✓ | TLS only |
| **PII (Email, Phone)** | AES-256 | ✓ | TLS only |
| **Vulnerability Details** | AES-256 | ✓ | TLS only |
| **Messages** | AES-256 | ✓ | TLS only |
| **Wallet Balance** | AES-256 | ✓ | TLS only |
| **Payment Methods** | AES-256 | ✓ | TLS only |
| **All API Responses** | N/A | N/A | TLS only |

**Encryption Algorithm**: AES-256-CBC with random IV per record

### 21.3 API Security

| Requirement | Implementation |
|------------|-----------------|
| **HTTPS/TLS** | Mandatory for all endpoints, minimum TLS 1.2 |
| **CSRF Protection** | Django CSRF middleware + `X-CSRFToken` header |
| **XSS Prevention** | Input sanitization + Content Security Policy (CSP) |
| **SQL Injection** | Parameterized queries (Django ORM) |
| **Rate Limiting** | 100 requests/minute per authenticated user |
| **CORS** | Whitelist specific frontend origin |
| **API Versioning** | `/api/v1/` prefix for version management |
| **Input Validation** | Zod schemas on frontend, Django serializers on backend |
| **Output Encoding** | JSON encoding with proper headers |

### 21.4 CSP Headers

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'unsafe-inline' cdn.example.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data:;
  font-src 'self';
  connect-src 'self' api.example.com;
  frame-ancestors 'none';
```

### 21.5 File Upload Security

| Requirement | Implementation |
|------------|-----------------|
| **File Type Validation** | MIME type + magic bytes validation |
| **File Size Limit** | Max 100MB per file |
| **Scan Integration** | ClamAV antivirus scanning |
| **Isolated Storage** | Files stored outside web root |
| **Filename Sanitization** | UUID naming, original filename encrypted |
| **Download Control** | Time-limited signed URLs with decryption |
| **Quarantine Process** | Suspicious files moved to quarantine folder |
| **Access Audit** | All file downloads logged with user info |

### 21.6 Audit & Compliance

| Requirement | Implementation |
|------------|-----------------|
| **Audit Logging** | All user actions logged to `AuditLog` model |
| **Immutable Logs** | Logs stored in append-only fashion |
| **Audit Trail Retention** | Minimum 2 years of audit logs |
| **Data Export** | Researchers can export their data (GDPR) |
| **Data Deletion** | Soft delete for PII, hard delete on request |
| **GDPR Compliance** | Privacy policy, consent management, data requests |
| **PCI DSS** | For payment processing (third-party processor) |

### 21.7 Infrastructure Security

| Component | Security Measure |
|-----------|-----------------|
| **Nginx** | Reverse proxy, SSL termination, gzip compression disabled for secrets |
| **Gunicorn** | Runs as non-root user, limited system access |
| **Database** | Password authentication, encrypted connections, automated backups |
| **Redis** | Authentication required, no persistence on sensitive data |
| **Environment Variables** | .env file with secrets, never committed to Git |
| **Docker** | Non-root container user, read-only root filesystem |

---

## 22. API Documentation Plan

### 22.1 Documentation Coverage

- **Interactive API Documentation**: Swagger UI at `/api/docs/`
- **Postman Collection**: Export API for team testing
- **API Response Examples**: All endpoints include sample requests/responses
- **Error Codes**: Standardized HTTP status codes + custom error codes
- **Rate Limit Headers**: Documented X-RateLimit-* headers
- **Authentication**: Bearer token format and refresh token flow
- **Webhooks**: Planned documentation for future webhook events

### 22.2 API Documentation Tools

- **Swagger/OpenAPI 3.0**: Automated from DRF schema
- **drf-spectacular**: Generates comprehensive OpenAPI schema
- **Tool**: Django Rest Framework's built-in documentation
- **Frontend**: ReDoc for beautiful API docs

### 22.3 Example API Endpoint Documentation Structure

```
POST /api/v1/reports

Description: Submit a new vulnerability report

Authentication: Required (Bearer Token)

Request Body:
{
  "program_id": "uuid",
  "title": "SQL Injection in Login Form",
  "description": "...",
  "vulnerability_type": "SQL_INJECTION",
  "severity": null,  # Triage team assigns
  "affected_url": "https://app.example.com/login",
  "steps_to_reproduce": [...],
  "cvss_vector": "CVSS:3.1/..."
}

Response (201 Created):
{
  "id": "uuid",
  "status": "SUBMITTED",
  "researcher_id": "uuid",
  "program_id": "uuid",
  "created_at": "2024-06-24T10:30:00Z",
  "updated_at": "2024-06-24T10:30:00Z"
}

Errors:
- 400: Invalid program_id or missing required fields
- 401: Unauthorized (not authenticated)
- 403: Forbidden (researcher not enrolled in program)
- 413: Payload too large (exceeds 500MB)
- 429: Rate limited (too many submissions)
```

---

## 23. Admin Panel Requirements

### 23.1 Admin Dashboard Views

| Page | Functionality |
|------|-----------------|
| **Dashboard Overview** | Key metrics, recent activity, alerts, system health |
| **User Management** | Search, view profiles, edit roles, suspend/delete accounts |
| **Organization Management** | View all companies, programs, team members |
| **Report Analytics** | Total reports, severity distribution, response times |
| **Audit Logs** | Full search and filtering of all user actions |
| **Dispute Resolution** | View open disputes, resolve payment disagreements |
| **Payment Monitoring** | Pending payouts, payment failures, reconciliation |
| **Content Moderation** | Flag/remove inappropriate reports or messages |
| **System Configuration** | Update severity tiers, reward ranges, SLAs |
| **Notifications** | Send system-wide announcements |

### 23.2 Admin Permissions Model

```
Admin User
├── View all users (read-only or edit)
├── Suspend/restore user accounts
├── View all organizations and programs
├── Override bounty decisions
├── View all reports and attachments
├── View full audit logs
├── Access dispute resolution
├── Configure system settings
└── Generate compliance reports
```

---

## 24. Development Roadmap

### Phase 1: MVP (Weeks 1-8)
**Goal**: Functional platform with core features for alpha testing

**Sprint 1-2: Foundation**
- User authentication and RBAC
- Researcher, Company, Triage user management
- Database schema implementation
- API endpoints for auth and profiles

**Sprint 3-4: Core Features**
- Program creation and management
- Vulnerability report submission
- Triage workflow (queue, assignment, status updates)
- In-app messaging system

**Sprint 5-6: Integration & Security**
- File upload and attachment handling
- Audit logging implementation
- Encryption for sensitive data
- Rate limiting and CORS

**Sprint 7-8: Frontend & Testing**
- Next.js dashboard for all user types
- End-to-end testing
- Performance optimization
- Security audit and hardening

### Phase 2: Beta (Weeks 9-12)
- Bounty and payment system
- Researcher reputation scoring
- Advanced duplicate detection
- Bug fixes from alpha feedback

### Phase 3: Production (Weeks 13+)
- S3 file storage migration
- Payment processor integration
- Load testing and scaling
- Public launch

---

## 25. Folder Structure

```
hackxharder/
│
├── backend/
│   ├── config/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   ├── production.py
│   │   │   └── testing.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   │
│   ├── apps/
│   │   ├── accounts/
│   │   ├── researchers/
│   │   ├── companies/
│   │   ├── reports/
│   │   ├── triage/
│   │   ├── messaging/
│   │   ├── payments/
│   │   ├── admin_panel/
│   │   ├── audit/
│   │   └── security/
│   │
│   ├── utils/
│   ├── tests/
│   ├── logs/
│   ├── media/           (local file storage)
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── store/
│   │   ├── types/
│   │   ├── styles/
│   │   └── middleware.ts
│   │
│   ├── public/
│   ├── tests/
│   ├── package.json
│   ├── next.config.js
│   ├── tsconfig.json
│   ├── .env.local.example
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── docker-compose.yml
├── nginx/
│   ├── nginx.conf
│   ├── Dockerfile
│   └── ssl/              (self-signed certs for dev)
│
├── docs/
│   ├── project-documentation.md
│   ├── API.md
│   ├── DATABASE.md
│   ├── SECURITY.md
│   ├── DEPLOYMENT.md
│   └── SETUP.md
│
├── .gitignore
├── README.md
└── .github/
    └── workflows/        (CI/CD pipelines)
        ├── test.yml
        ├── lint.yml
        └── deploy.yml
```

---

## 26. Environment Variables Example

### Backend (.env.example)
```
# Django Settings
DEBUG=False
SECRET_KEY=your-secret-key-here-min-50-chars
ALLOWED_HOSTS=localhost,127.0.0.1,app.example.com
DJANGO_SETTINGS_MODULE=config.settings.development

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=hackxharder_db
DB_USER=postgres
DB_PASSWORD=secure_password
DB_HOST=db
DB_PORT=5432

# Redis
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/1
CELERY_RESULT_BACKEND=redis://redis:6379/2

# Security
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://app.example.com
CSRF_TRUSTED_ORIGINS=http://localhost:3000,https://app.example.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000

# Email (for notifications)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=noreply@hackxharder.com
EMAIL_HOST_PASSWORD=your-app-password

# File Upload
MAX_UPLOAD_SIZE_MB=100
ALLOWED_FILE_TYPES=pdf,png,jpg,gif,txt,zip,rar

# Encryption
ENCRYPTION_KEY=base64-encoded-32-byte-key

# Payment Processing
STRIPE_API_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...

# AWS S3 (future)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=us-east-1

# Logging
LOG_LEVEL=INFO
SENTRY_DSN=

# Rate Limiting
RATELIMIT_ENABLE=True
```

### Frontend (.env.local.example)
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_APP_NAME=HackXHarder
NEXT_PUBLIC_APP_VERSION=1.0.0
NEXT_PUBLIC_ENVIRONMENT=development

# Optional: Analytics
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID=
NEXT_PUBLIC_MIXPANEL_TOKEN=
```

---

## 27. Local Development Setup Guide

### 27.1 Prerequisites

```bash
# Verify installations
python --version      # 3.10+
node --version       # 18+
npm --version        # 9+
docker --version     # 24+
git --version        # 2.40+
```

### 27.2 Initial Setup

```bash
# Clone repository
git clone https://github.com/your-org/hackxharder.git
cd hackxharder

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Backend setup
cd backend
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data  # Optional: load sample data

# Frontend setup
cd ../frontend
npm install
cp .env.local.example .env.local

# Return to root
cd ..
```

### 27.3 Running Development Server

**Terminal 1 - Backend API**:
```bash
cd backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

**Terminal 2 - Frontend**:
```bash
cd frontend
npm run dev
# Accessible at http://localhost:3000
```

**Terminal 3 - Celery Worker** (optional):
```bash
cd backend
source venv/bin/activate
celery -A config worker -l info
```

**Terminal 4 - Redis** (if not using Docker):
```bash
redis-server
```

---

## 28. Docker Development Setup Guide

### 28.1 Docker Compose File

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: hackxharder_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7
    ports:
      - "6379:6379"

  backend:
    build: ./backend
    command: >
      sh -c "python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000"
    environment:
      - DEBUG=True
      - SECRET_KEY=dev-secret-key
      - DB_HOST=db
      - REDIS_URL=redis://redis:6379/0
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    depends_on:
      - db
      - redis

  frontend:
    build: ./frontend
    command: npm run dev
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app

  nginx:
    build: ./nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
    depends_on:
      - backend
      - frontend

volumes:
  postgres_data:
```

### 28.2 Running with Docker

```bash
# Build and start all services
docker-compose up --build

# Verify services
docker-compose ps

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop all services
docker-compose down

# Clean up volumes
docker-compose down -v
```

---

## 29. Production Deployment Plan

### 29.1 Pre-Deployment Checklist

- [ ] All tests passing (unit, integration, e2e)
- [ ] Security audit completed
- [ ] Environment variables configured for production
- [ ] Database backups enabled
- [ ] HTTPS certificates obtained (Let's Encrypt)
- [ ] Email service configured (SendGrid, Mailgun)
- [ ] Payment processor keys configured (Stripe)
- [ ] CDN configured for static assets
- [ ] Monitoring and alerting set up (Sentry, DataDog)
- [ ] Disaster recovery plan documented

### 29.2 Deployment Environment

**Server Requirements**:
- OS: Ubuntu 22.04 LTS
- RAM: 16GB minimum
- CPU: 4 cores minimum
- Storage: 500GB SSD
- Network: Static IP, ports 80/443 open

**Recommended Hosting**: AWS EC2, DigitalOcean, Heroku, or Railway

### 29.3 Production Deployment Steps

```bash
# 1. Provision server and SSH in
ssh ubuntu@your-server-ip

# 2. Install dependencies
sudo apt update && sudo apt install -y \
  docker.io docker-compose nginx postgresql-client git

# 3. Clone repository
git clone https://github.com/your-org/hackxharder.git
cd hackxharder

# 4. Configure environment variables
nano backend/.env
nano frontend/.env.production

# 5. Build Docker images
docker-compose -f docker-compose.prod.yml build

# 6. Run migrations
docker-compose -f docker-compose.prod.yml run backend \
  python manage.py migrate

# 7. Collect static files
docker-compose -f docker-compose.prod.yml run backend \
  python manage.py collectstatic --noinput

# 8. Start services
docker-compose -f docker-compose.prod.yml up -d

# 9. Verify health
curl -I https://your-domain.com
```

### 29.4 Monitoring & Alerts

**Monitoring Tools**:
- **Sentry**: Application error tracking
- **DataDog**: Infrastructure and APM monitoring
- **UptimeRobot**: Uptime monitoring
- **CloudFlare**: DDoS protection

**Key Metrics to Monitor**:
- API response time (target: <200ms)
- Database query time (target: <100ms)
- Error rate (target: <0.5%)
- CPU usage (alert if >80%)
- Memory usage (alert if >85%)
- Disk space (alert if >90%)
- 5xx errors (alert if any)

---

## 30. Testing Strategy

### 30.1 Test Coverage Goals

| Test Type | Coverage Target | Tools |
|-----------|-----------------|-------|
| Unit Tests | 80% | Jest, Pytest, unittest |
| Integration Tests | 60% | Pytest-Django, React Testing Library |
| E2E Tests | 40% critical paths | Playwright, Cypress |
| Security Tests | 100% | OWASP ZAP, Bandit |
| Load Tests | Baseline established | Locust, Apache JMeter |

### 30.2 Backend Testing

**Unit Tests** (app/tests/test_models.py):
```python
# Test Report model validation
# Test Bounty calculation logic
# Test Permission checks
```

**Integration Tests** (tests/integration/):
```python
# Test full report submission flow
# Test triage workflow
# Test payment processing
```

**API Tests**:
```python
# Test all endpoints with valid/invalid input
# Test authentication and authorization
# Test rate limiting
```

### 30.3 Frontend Testing

**Unit Tests** (src/__tests__/):
```typescript
// Test components render correctly
// Test hooks and custom logic
// Test utility functions
```

**Integration Tests**:
```typescript
// Test form submission flow
// Test API integration
// Test state management
```

**E2E Tests** (tests/e2e/):
```typescript
// Test researcher report submission flow
// Test triage team workflow
// Test payment process
```

### 30.4 Security Testing

**OWASP Top 10 Verification**:
- [ ] Injection attacks (SQLi, XSS)
- [ ] Broken authentication
- [ ] Sensitive data exposure
- [ ] Access control bypass
- [ ] Security misconfiguration
- [ ] CSRF vulnerabilities
- [ ] Insecure deserialization
- [ ] Using components with known vulnerabilities
- [ ] Insufficient logging/monitoring
- [ ] API misuse

---

## 31. Logging and Audit Trail

### 31.1 Audit Log Implementation

**Logged Events**:
- User login/logout
- Report submission
- Report status changes
- Triage assignments
- Bounty approvals
- Data access (files, sensitive fields)
- Administrative actions
- Failed login attempts
- Permission changes

**Audit Log Schema**:
```python
class AuditLog(models.Model):
    user = ForeignKey(User, null=True)
    action_type = CharField(choices=ACTION_TYPES)
    content_type = CharField()
    object_id = CharField()
    changes = JSONField()  # {field: {old_value, new_value}}
    ip_address = CharField()
    user_agent = CharField()
    status = CharField(choices=['SUCCESS', 'FAILURE'])
    timestamp = DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [Index(fields=['user', 'timestamp'])]
```

### 31.2 Log Retention and Compliance

- **Retention Period**: 2 years minimum
- **Compliance**: GDPR, SOC 2, applicable regulations
- **Access**: Only Platform Admin can query audit logs
- **Export**: Audit reports generated for compliance audits
- **Immutability**: No deletion, only append-only operations

### 31.3 Logging Levels

| Level | Examples | Retention |
|-------|----------|-----------|
| **DEBUG** | API request details, caching info | 7 days |
| **INFO** | User actions, report status changes | 2 years |
| **WARNING** | Rate limit exceeded, validation failures | 1 year |
| **ERROR** | Failed payment processing, DB connection errors | 2 years |
| **CRITICAL** | Security breach attempts, authentication failures | 2 years |

---

## 32. Backup and Recovery Plan

### 32.1 Backup Strategy

**Database Backups**:
- **Frequency**: Daily automated backups
- **Retention**: 30-day rolling window
- **Storage**: S3 with versioning enabled
- **Encryption**: AES-256 at rest

**File Storage Backups**:
- **Frequency**: Daily incremental, weekly full
- **Retention**: 30-day rolling window
- **Storage**: Separate S3 bucket with replication

**Backup Verification**:
- Monthly restore test to separate environment
- Automated backup integrity checks
- Documented recovery procedures

### 32.2 Disaster Recovery

**RTO/RPO Targets**:
- **RTO** (Recovery Time Objective): 4 hours
- **RPO** (Recovery Point Objective): 1 hour

**Failover Procedure**:
1. Detect outage via monitoring alerts
2. Provision new database from latest backup
3. Restore file attachments from S3
4. Update DNS to new server
5. Verify all systems operational
6. Post-incident review

### 32.3 Data Retention Policies

| Data Type | Retention | Notes |
|-----------|-----------|-------|
| Active Reports | Permanent | Research disclosure history |
| Audit Logs | 2 years | Compliance requirement |
| User Activity | 1 year | After account deletion |
| Backups | 30 days | Rolling window |
| Error Logs | 90 days | Troubleshooting |
| Deleted Attachments | 30 days | Recovery window |

---

## 33. Documentation Roadmap

### Phase 1: MVP Documentation (Concurrent with Dev)
- ✓ Developer documentation (this file)
- ✓ API documentation with Swagger
- ✓ Database schema documentation
- ✓ Security requirements documentation
- Setup guide for developers
- Deployment guide

### Phase 2: Beta Documentation
- API client library documentation
- Administrator guide
- Researcher user guide
- Company admin guide
- Contributing guidelines

### Phase 3: Production Documentation
- System architecture deep-dive
- SLA and uptime monitoring
- Incident response procedures
- Data privacy and compliance
- Performance tuning guide
- Scaling guidelines

---

## 34. Final Summary

### 34.1 Project Readiness Checklist

**Architecture**:
- ✓ Full-stack architecture defined
- ✓ Technology stack selected and justified
- ✓ Database schema designed
- ✓ API endpoints planned
- ✓ Security model documented

**Development**:
- ✓ Folder structure established
- ✓ Environment configuration templates created
- ✓ Development and Docker setup guides provided
- ✓ Testing strategy defined
- ✓ CI/CD pipeline structure outlined

**Security**:
- ✓ Encryption strategy defined for all sensitive data
- ✓ RBAC system designed with 4 user roles
- ✓ Audit logging system planned
- ✓ File upload security requirements specified
- ✓ API security measures detailed

**Operations**:
- ✓ Production deployment plan created
- ✓ Backup and recovery procedures documented
- ✓ Monitoring and alerting strategy defined
- ✓ Logging and compliance requirements specified
- ✓ Disaster recovery procedures outlined

### 34.2 MVP Feature Priority

**Week 1-4 (Core)**:
1. User authentication and RBAC
2. Program creation and scope definition
3. Report submission and validation
4. Basic triage workflow

**Week 5-8 (Polish)**:
1. File attachments and uploads
2. Messaging system
3. Frontend UI/UX
4. Testing and security hardening

### 34.3 Key Success Metrics

- **User Adoption**: 100 researchers and 10 companies by month 3
- **Report Quality**: 80%+ of submitted reports are valid (non-rejected)
- **Response Time**: Average 48-hour first response to reports
- **System Uptime**: 99.5% availability
- **Security**: Zero data breaches, 100% audit log coverage
- **Performance**: API response time <200ms at p95

### 34.4 Next Steps

1. **Infrastructure Setup**: Set up PostgreSQL, Redis, and file storage
2. **Backend Development**: Implement Django app structure and core models
3. **Frontend Development**: Build React components and pages
4. **Integration**: Connect frontend and backend APIs
5. **Testing**: Unit, integration, and security testing
6. **Deployment**: Configure Docker and deploy to development environment
7. **Feedback**: Internal testing and iteration
8. **Launch**: Deploy to production

---

## 35. Appendix: Key Technologies

### Django REST Framework
- Serialization for API responses
- Authentication via JWT tokens
- Pagination and filtering
- Auto-generated API documentation

### Next.js
- Server-side rendering for SEO
- API routes for backend integration
- Built-in optimization and performance
- TypeScript support

### PostgreSQL
- ACID compliance for data integrity
- Advanced indexing for performance
- Full-text search capabilities
- JSONB for flexible schema fields

### Redis
- Caching layer for performance
- Job queue for asynchronous tasks
- Session storage
- Rate limiting counters

### Docker
- Consistent development environment
- Easy scaling for production
- Version control of infrastructure
- Simplified deployment process

---

**Document Version**: 1.0  
**Last Updated**: 2026-06-24  
**Status**: Complete MVP Specification  
**Author**: HackXHarder Development Team  

---

*This documentation serves as the complete technical specification for HackXHarder development. All architectural decisions, security requirements, and implementation guidelines herein should be followed throughout the development lifecycle.*
