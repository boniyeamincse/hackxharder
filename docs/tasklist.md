# HackXHarder Project Tasklist

**MVP Target**: 8 weeks (Phase 1)  
**Status**: Not started  
**Owner**: Boni Yeamin

---

## PHASE 1: MVP (Weeks 1–8)

### Sprint 1–2: Foundation & Auth (Weeks 1–2)

#### Backend Setup
- [ ] Initialize Django project structure (config/, apps/, utils/)
- [ ] Set up PostgreSQL database config (base, dev, prod, test settings)
- [ ] Configure Redis connection (cache + Celery broker)
- [ ] Create .env template (DB, Redis, encryption key, CORS, email)
- [ ] Set up Celery + beat scheduler config
- [ ] Create base requirements.txt (Django 4.x, DRF, psycopg2, redis, celery, etc.)
- [ ] Initialize Docker setup (Dockerfile, docker-compose.yml for local dev)
- [ ] Create Nginx reverse proxy config (self-signed SSL for dev)

#### Database & Models (accounts app)
- [ ] Create extended User model (AbstractUser)
- [ ] Create Profile model (role enum: RESEARCHER, COMPANY_ADMIN, TRIAGE_LEAD, ADMIN)
- [ ] Create 2FA model (TOTP secrets, enabled flag, backup codes)
- [ ] Write model migrations
- [ ] Create model factories for testing

#### Authentication API (accounts app)
- [ ] POST /api/v1/auth/register — register user (email, password, role)
- [ ] POST /api/v1/auth/login — JWT token + refresh token
- [ ] POST /api/v1/auth/logout — invalidate session
- [ ] POST /api/v1/auth/refresh-token — refresh JWT
- [ ] POST /api/v1/auth/2fa/setup — generate TOTP secret, return QR code
- [ ] POST /api/v1/auth/2fa/verify — verify code + enable 2FA
- [ ] POST /api/v1/auth/password-reset — send reset email (24h link)
- [ ] POST /api/v1/auth/password-reset/confirm — reset password with token
- [ ] Implement JWT middleware + token expiry (15min access, 7d refresh)
- [ ] Create rate limiting decorator (10/min per IP for login)
- [ ] Create RBAC decorators (@require_role, @require_permission)

#### Frontend Setup
- [ ] Initialize Next.js 14+ project (App Router, TypeScript)
- [ ] Set up Tailwind CSS + shadcn/ui
- [ ] Create .env.local template (API URL, app version, environment)
- [ ] Initialize Redux Toolkit store + auth slice
- [ ] Create axios client with interceptors (JWT refresh logic)
- [ ] Set up Jest + React Testing Library
- [ ] Create middleware.ts for auth checks
- [ ] Install form dependencies (React Hook Form, Zod)

#### Frontend Auth Pages
- [ ] Create src/app/auth/login/page.tsx (form, 2FA prompt)
- [ ] Create src/app/auth/register/page.tsx (form, role selection)
- [ ] Create src/app/auth/2fa/page.tsx (TOTP setup, verification)
- [ ] Create src/app/auth/password-reset/page.tsx (email form)
- [ ] Create LoginForm, RegisterForm, TwoFactorSetup components
- [ ] Create useAuth hook (login, logout, user state)
- [ ] Create auth guards (redirect to login if not authenticated)

#### Testing (Weeks 1–2)
- [ ] Write unit tests for User model (creation, password hashing)
- [ ] Write tests for JWT token generation + refresh
- [ ] Write tests for RBAC decorators (permission checks)
- [ ] Write integration tests for /auth/* endpoints
- [ ] Write frontend component tests for login/register forms

---

### Sprint 3–4: Core Features (Weeks 3–4)

#### Researcher & Company Models (researcher app, companies app)
- [ ] Create Researcher model (reputation_score, verified, submission_count, avg_rating)
- [ ] Create Company model (name, logo, industry, size, subscription_tier)
- [ ] Create Program model (name, type: VDP|BUG_BOUNTY, status, scope JSONB, rules)
- [ ] Create Scope model (domain, scope_type: IN_SCOPE|OUT_OF_SCOPE, description)
- [ ] Create SeverityLevel model (level, CVSS range, reward range per program)
- [ ] Write migrations + factories

#### Researcher Profile API (researchers app)
- [ ] GET /api/v1/researchers/profile — fetch user profile
- [ ] PUT /api/v1/researchers/profile — update bio, location, avatar
- [ ] GET /api/v1/researchers/programs — list enrolled programs
- [ ] GET /api/v1/researchers/reports — list researcher's reports (paginated)
- [ ] GET /api/v1/researchers/earnings — total bounty earned, pending
- [ ] GET /api/v1/researchers/wallet — wallet balance + payment methods

#### Company & Program API (companies app)
- [ ] POST /api/v1/programs — create new program (company admin only)
- [ ] GET /api/v1/programs — list all active programs (public + enrolled)
- [ ] GET /api/v1/programs/{id} — program details + scope
- [ ] PUT /api/v1/programs/{id} — update program (owner only)
- [ ] DELETE /api/v1/programs/{id} — soft delete program (owner only)
- [ ] POST /api/v1/programs/{id}/scope — add/update scope items
- [ ] GET /api/v1/programs/{id}/team — list team members + roles
- [ ] POST /api/v1/programs/{id}/team/invite — invite triage member

#### Report & Triage Models (reports app, triage app)
- [ ] Create Report model (title, description, status, severity, CVSS, created_at)
- [ ] Create Attachment model (file_path, MIME, size, scan_status, uploaded_by)
- [ ] Create Comment model (text, is_internal, created_at)
- [ ] Create TriageAssignment model (report, triage_user, priority, assigned_at, due_date)
- [ ] Create StatusHistory model (report, old_status, new_status, changed_by, reason)
- [ ] Add unique constraint: (researcher, program, vulnerability_hash)
- [ ] Write migrations + factories

#### Report Submission API (reports app)
- [ ] POST /api/v1/reports — submit vulnerability report (form validation)
- [ ] GET /api/v1/reports/{id} — fetch report + comments (auth check)
- [ ] PUT /api/v1/reports/{id} — update report (researcher only, before triage)
- [ ] GET /api/v1/reports/{id}/comments — list comments (threaded?)
- [ ] POST /api/v1/reports/{id}/comments — add comment (encrypted if sensitive)
- [ ] Implement auto-validation task (Celery): check scope, format, duplicate hash
- [ ] Create serializers + validators (title length, description min/max, etc.)

#### Triage Workflow API (triage app)
- [ ] GET /api/v1/triage/queue — list assigned reports (filtered by status, priority)
- [ ] PUT /api/v1/triage/reports/{id}/status — update status (TRIAGING → VALIDATED/REJECTED/DUPLICATE)
- [ ] POST /api/v1/triage/reports/{id}/severity — assign CVSS + severity level
- [ ] PUT /api/v1/triage/reports/{id}/assign — reassign to team member
- [ ] POST /api/v1/triage/reports/{id}/notes — add internal notes (hidden from researcher)
- [ ] Implement duplicate detection service (hash-based + optional heuristics for MVP)

#### Frontend Pages (Weeks 3–4)
- [ ] Create src/app/dashboard/researcher/page.tsx (submissions list, earnings, messages)
- [ ] Create src/app/dashboard/company/page.tsx (programs, team, analytics preview)
- [ ] Create src/app/dashboard/triage/page.tsx (queue, filters, assignment)
- [ ] Create src/app/programs/page.tsx (browse programs, search, filter)
- [ ] Create src/app/programs/[id]/page.tsx (program details, scope, rules, enroll)
- [ ] Create src/app/programs/[id]/submit/page.tsx (report form, file upload preview)
- [ ] Create src/app/reports/[id]/page.tsx (report detail, comments, status timeline)

#### Frontend Components (Weeks 3–4)
- [ ] Create ReportSubmissionForm (title, description, affected_url, attachment uploader)
- [ ] Create ProgramCreationForm (name, type, scope, rules)
- [ ] Create TriageForm (status dropdown, severity selector, internal notes)
- [ ] Create ProgramCard (name, type, scope count, reward tier)
- [ ] Create ReportCard (title, status badge, severity, created_at)
- [ ] Create ReportList (paginated, sortable, filterable)
- [ ] Create TriageQueue (report list, filters by status/severity/assigned)
- [ ] Create Navbar + Sidebar (nav based on role)

#### Testing (Weeks 3–4)
- [ ] Integration tests: full report submission flow
- [ ] Integration tests: triage workflow (assign → assess → validate)
- [ ] API tests: permission checks (researchers can't access triage queue, etc.)
- [ ] Frontend component tests: forms render + validate input

---

### Sprint 5–6: File Upload & Messaging (Weeks 5–6)

#### File Upload & Security (reports app, security app)
- [ ] Create Attachment model + migration
- [ ] Implement file type validation (whitelist: PDF, PNG, JPG, GIF, TXT, ZIP, RAR)
- [ ] Implement file size limits (100MB per file, 500MB per report)
- [ ] Create file upload endpoint: POST /api/v1/reports/{id}/attachments
- [ ] Implement ClamAV integration (placeholder for dev, real for prod)
- [ ] Create encrypted file storage handler (UUID naming, local path)
- [ ] Create signed download URL generator (time-limited, encrypted)
- [ ] GET /api/v1/reports/{id}/attachments/{file-id} — download (auth + audit log)
- [ ] Create attachment audit logging (who downloaded, when, IP)
- [ ] Implement quarantine logic (suspicious files → admin review)

#### Encryption (security app)
- [ ] Create AES-256-CBC encryption utilities (encrypt_field, decrypt_field)
- [ ] Define encrypted fields: 2FA secrets, PII (email optional), wallet balance, payment methods, messages, vulnerability details
- [ ] Create EncryptedField model field (Django custom field for transparency)
- [ ] Test encryption/decryption round-trips

#### Messaging & Notification Models (messaging app, audit app)
- [ ] Create Conversation model (report FK, participants ManyToMany, subject, created_at)
- [ ] Create Message model (conversation FK, sender FK, content encrypted, read_by ManyToMany)
- [ ] Create NotificationPreference model (user, frequency, channels, quiet hours)
- [ ] Create AuditLog model (user, action_type, content_type, object_id, changes JSONB, IP, user_agent, status, timestamp)

#### Messaging API (messaging app)
- [ ] GET /api/v1/messages — list conversations (paginated)
- [ ] POST /api/v1/messages — start new conversation (for report, creates auto-conversation)
- [ ] GET /api/v1/conversations/{id} — fetch conversation + messages
- [ ] POST /api/v1/conversations/{id}/messages — add message (encrypt content)
- [ ] Mark message as read (update read_by)
- [ ] Create Celery task: send email notification on new message (respects prefs)

#### Audit Logging Middleware (audit app)
- [ ] Create AuditMiddleware: log all POST/PUT/DELETE requests
- [ ] Capture: user, action (CREATE/UPDATE/DELETE/DOWNLOAD), model, object_id, before/after values, IP, user_agent
- [ ] Log authentication events (LOGIN/LOGOUT/2FA)
- [ ] Log permission-denied attempts (FAILURE status)
- [ ] Create audit log API: GET /api/v1/admin/audit-logs (admin only, searchable, filterable)

#### Frontend Messaging UI (Weeks 5–6)
- [ ] Create src/app/messages/page.tsx (conversation list)
- [ ] Create src/app/messages/[id]/page.tsx (conversation thread)
- [ ] Create MessageList component (messages, timestamps, read status)
- [ ] Create MessageComposer component (textarea, send button, typing indicator)
- [ ] Create ConversationList component (preview, unread count)
- [ ] Implement WebSocket or polling for real-time messages (polling for MVP)

#### Frontend File Upload UI (Weeks 5–6)
- [ ] Create AttachmentUploader component (drag-drop, file list, progress bar)
- [ ] Implement file validation on frontend (type, size, count)
- [ ] Create attachment preview in report detail (download link, scan status badge)

#### Testing (Weeks 5–6)
- [ ] Test file upload (valid + invalid types, size limits)
- [ ] Test ClamAV integration (mock antivirus response)
- [ ] Test encryption/decryption for all encrypted fields
- [ ] Test messaging (create conversation, add message, mark read)
- [ ] Test audit logging (verify all actions logged, sensitive data masked)

---

### Sprint 7–8: Admin, Security Hardening, Polish (Weeks 7–8)

#### Admin Panel Models & API (admin_panel app)
- [ ] Create AdminAction model (admin, action, target_user/object, reason, timestamp)
- [ ] Create Dispute model (report FK, raised_by, reason, resolved, resolution)
- [ ] Create SystemConfig model (severity tiers, SLA targets, max_file_size, etc.)

#### Admin API (admin_panel app)
- [ ] GET /api/v1/admin/users — list all users (search, filter by role)
- [ ] GET /api/v1/admin/users/{id} — user detail + activity
- [ ] POST /api/v1/admin/users/{id}/suspend — suspend account
- [ ] POST /api/v1/admin/users/{id}/restore — restore suspended account
- [ ] GET /api/v1/admin/audit-logs — full audit log search + export
- [ ] GET /api/v1/admin/reports — report analytics (count by status, severity, response time)
- [ ] POST /api/v1/admin/disputes/{id}/resolve — resolve payment/bounty dispute
- [ ] GET /api/v1/admin/system-config — get + PUT system settings

#### Security Hardening (Weeks 7–8)
- [ ] Add CSRF protection (Django middleware + X-CSRFToken header)
- [ ] Add XSS prevention (input sanitization, output encoding, CSP headers)
- [ ] Add SQL injection prevention (verify all ORM queries are parameterized)
- [ ] Implement account lockout (5 failed attempts → 15min lock)
- [ ] Implement password complexity rules (12+ chars, numbers, symbols)
- [ ] Set up HTTPS/TLS (self-signed for dev, Let's Encrypt for prod)
- [ ] Add rate limiting decorators to all public endpoints (100 req/min auth, 10 req/min login)
- [ ] Implement secure session timeouts (15min idle)
- [ ] Add security headers (HSTS, X-Frame-Options, X-Content-Type-Options, CSP)
- [ ] Test for common vulnerabilities (OWASP ZAP or Burp scan)

#### Frontend Security & Polish (Weeks 7–8)
- [ ] Implement CSP headers in Next.js config
- [ ] Add error boundaries for graceful error handling
- [ ] Create global loading spinner + error toast UI
- [ ] Implement proper 404 + 500 error pages
- [ ] Add form validation + error messages
- [ ] Create success/warning/error toast notifications
- [ ] Implement redirect after logout
- [ ] Test accessibility (keyboard nav, screen reader compat, color contrast)

#### Frontend Admin Dashboard (Weeks 7–8)
- [ ] Create src/app/admin/page.tsx (overview: key metrics, recent activity, alerts)
- [ ] Create src/app/admin/users/page.tsx (user list, search, filter, suspend/restore)
- [ ] Create src/app/admin/audit/page.tsx (audit log viewer, search, export)
- [ ] Create src/app/admin/disputes/page.tsx (dispute list, resolution form)

#### Email Notifications (Weeks 7–8)
- [ ] Set up email backend (SMTP: Gmail/SendGrid/Mailgun)
- [ ] Create email templates (report submitted, status changed, bounty approved, payout processed)
- [ ] Create Celery tasks: send_notification_email, send_report_submitted_email, etc.
- [ ] Implement email preference checks (skip if user opted out)

#### Testing & QA (Weeks 7–8)
- [ ] Unit tests: all serializers, validators, service functions (target 80% coverage)
- [ ] Integration tests: critical user flows (researcher → submit → triage → bounty)
- [ ] API tests: all endpoints with valid/invalid input, auth checks, rate limiting
- [ ] Security tests: SQLi, XSS, CSRF, auth bypass, privilege escalation
- [ ] Frontend unit tests: components, hooks, utility functions (target 60% coverage)
- [ ] Frontend integration tests: form submission, API integration, state management
- [ ] E2E tests: researcher report flow, triage workflow, admin user suspension (Playwright/Cypress)
- [ ] Manual testing: all user roles, edge cases, error scenarios

#### Documentation (Weeks 7–8)
- [ ] Update API documentation (Swagger/OpenAPI, add all endpoints)
- [ ] Create developer setup guide (local dev, Docker, requirements)
- [ ] Create deployment guide (prod checklist, environment config)
- [ ] Document database schema (ERD, model relationships)
- [ ] Document security measures (encryption, RBAC, audit trail)
- [ ] Create troubleshooting guide (common errors, logs)

#### Docker & CI/CD Setup (Weeks 7–8)
- [ ] Create Dockerfile for backend (Python 3.10, deps, non-root user)
- [ ] Create Dockerfile for frontend (Node 18, Next.js build)
- [ ] Update docker-compose.yml (services: db, redis, backend, frontend, nginx)
- [ ] Create GitHub Actions workflows:
  - [ ] test.yml (run unit + integration tests on push)
  - [ ] lint.yml (code style, type checking)
  - [ ] security.yml (dependency audit, SAST)
- [ ] Set up pre-commit hooks (black, eslint, migrations check)

---

## PHASE 2: Beta (Weeks 9–12)

### Payment & Bounty System
- [ ] Create Bounty model (report FK, amount, currency, status: PENDING|APPROVED|PAID|REJECTED, approved_by, approved_date, paid_date)
- [ ] Create Wallet model (researcher FK, balance encrypted, currency, last_updated)
- [ ] Create PaymentMethod model (researcher FK, type: BANK_TRANSFER|CRYPTO|PAYPAL, details encrypted, verified)
- [ ] Create Payout model (wallet FK, payment_method FK, amount, status, transaction_id, timestamps)
- [ ] Implement bounty calculation logic (lookup tier by severity + program rules)
- [ ] Create bounty approval workflow (auto-approve vs. manual)
- [ ] Implement duplicate bounty handling (configurable: first-only or reduced payouts)
- [ ] Create Celery task: process_payouts (batch payout processing)
- [ ] Integrate with payment processor (Stripe or similar for MVP placeholder)
- [ ] API: GET /api/v1/payments/wallet, POST /api/v1/payments/method, GET /api/v1/payments/history

### Advanced Duplicate Detection
- [ ] Implement heuristic-based duplicate detection (keyword similarity, scope overlap)
- [ ] Optional: Add ML model for duplicate scoring (future phase, MVP placeholder)
- [ ] Create API to flag + link duplicates (triage only)

### Researcher Reputation System
- [ ] Add reputation_score field to Researcher model
- [ ] Implement scoring logic: +points for validated reports, -points for rejected/duplicates
- [ ] Create reputation tier badges (new, verified, trusted, expert)
- [ ] Display reputation in researcher profile + leaderboard preview

### Enhanced Admin & Reporting
- [ ] Create admin reporting API (CSV export: reports, users, payouts)
- [ ] Implement dispute resolution workflow (SLA tracking, escalation)
- [ ] Create content moderation tools (flag inappropriate reports/messages)

### Bug Fixes & Refinement
- [ ] Gather alpha feedback + prioritize bugs
- [ ] Fix security findings from pentesting
- [ ] Optimize slow queries (add database indexes as needed)
- [ ] Polish UI/UX (colors, spacing, typography, animations)

---

## PHASE 3: Production (Weeks 13+)

### Infrastructure & Scaling
- [ ] Migrate file storage from local → AWS S3
- [ ] Set up CloudFront CDN for static assets
- [ ] Configure S3 lifecycle policies (archive old attachments)
- [ ] Implement database backups (daily automated, 30-day retention)
- [ ] Set up monitoring (Sentry for errors, DataDog for APM, UptimeRobot for uptime)
- [ ] Configure alerting (Slack notifications, email escalation)
- [ ] Load testing (establish baseline performance metrics)

### Payment Processor Integration
- [ ] Integrate real Stripe/PayPal/Wise (remove placeholder)
- [ ] Implement PCI DSS compliance for payment processing
- [ ] Create payment reconciliation reports
- [ ] Test payout workflows end-to-end

### Compliance & Security
- [ ] Complete security audit (third-party pentesting)
- [ ] Implement GDPR data export + deletion workflows
- [ ] Create privacy policy + terms of service
- [ ] Set up legal frameworks for bounty agreements
- [ ] Audit encryption key management (rotate keys regularly)

### Public Launch
- [ ] Create marketing website (landing page, blog, docs)
- [ ] Set up support channels (email, Slack, knowledge base)
- [ ] Migrate to production database + server
- [ ] Configure domain + SSL certificates
- [ ] Set up monitoring dashboards
- [ ] Create runbook for oncall support
- [ ] Launch to public beta → full production

---

## Post-Production Roadmap

### Phase 2: Advanced Features
- [ ] Automated vulnerability timeline enforcement
- [ ] CVE publication + vulnerability database integration
- [ ] Advanced analytics dashboard (vulnerability trends, researcher leaderboard)
- [ ] Custom report templates per organization
- [ ] REST API for third-party integrations
- [ ] Mobile app (React Native)

### Phase 3: Integrations
- [ ] Slack bot for triage notifications
- [ ] Jira integration for ticket creation
- [ ] GitHub integration for disclosure timeline
- [ ] Webhook system for custom integrations
- [ ] Email digest notifications (weekly summary)

### Phase 4: Machine Learning
- [ ] Automated severity recommendation (ML model)
- [ ] Duplicate detection with ML
- [ ] Remediation suggestions (based on vuln type)
- [ ] Researcher skill-matching (recommend programs)

### Phase 5: Advanced Security
- [ ] Proof-of-concept sandbox environment (isolate code execution)
- [ ] Fuzzing tools for researchers
- [ ] SOC 2 Type II compliance
- [ ] Advanced encryption key management (Vault)
- [ ] Multi-region deployment (disaster recovery)

---

## Cross-Cutting Concerns

### All Phases
- [ ] Git workflow: feature branches, PR reviews, squash commits
- [ ] Code style: Black (Python), Prettier (JS/TS)
- [ ] Type checking: mypy (Python), TypeScript (frontend)
- [ ] Commit message format: Conventional Commits
- [ ] Logging: structured JSON logs, 2-year audit retention
- [ ] Monitoring: error tracking, performance metrics, uptime
- [ ] Documentation: keep code comments minimal, update docs with changes
- [ ] Accessibility: WCAG 2.1 AA compliance (keyboard nav, color contrast, screen readers)
- [ ] Performance: API <200ms p95, frontend <3s initial load
- [ ] Scalability: design for 1M+ reports, 100K+ researchers, 10K+ companies

---

## Success Metrics (MVP)

- [ ] All unit tests passing (80%+ coverage backend, 60%+ frontend)
- [ ] All integration tests passing (critical flows: submit → triage → bounty)
- [ ] Zero critical security findings in pentesting
- [ ] API response time <200ms (p95)
- [ ] Frontend initial load <3s
- [ ] Uptime 99.5% in staging
- [ ] Zero unhandled exceptions in production
- [ ] 100% audit log coverage (all user actions logged)
- [ ] All documentation complete + reviewed
- [ ] Ready for alpha testing with 5–10 orgs + 50–100 researchers
