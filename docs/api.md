# HackXHarder API Documentation

**Base URL**: `https://api.example.com/api/v1/`  
**Authentication**: Bearer Token (JWT)  
**Format**: JSON  
**Version**: 1.0

---

## Table of Contents

1. [Authentication](#authentication)
2. [Researcher Endpoints](#researcher-endpoints)
3. [Company Endpoints](#company-endpoints)
4. [Program Endpoints](#program-endpoints)
5. [Report Endpoints](#report-endpoints)
6. [Triage Endpoints](#triage-endpoints)
7. [Messaging Endpoints](#messaging-endpoints)
8. [Payment Endpoints](#payment-endpoints)
9. [Admin Endpoints](#admin-endpoints)
10. [Error Codes](#error-codes)
11. [Rate Limiting](#rate-limiting)

---

## Authentication

### Register User

**POST** `/auth/register/`

Register new researcher or company admin account.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!",
  "role": "researcher"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "role": "researcher",
  "created_at": "2026-06-24T10:30:00Z"
}
```

**Errors:**
- `400`: Invalid email format, weak password, role not recognized
- `409`: Email already registered

---

### Login

**POST** `/auth/login/`

Authenticate user and receive access/refresh tokens.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!"
}
```

**Response:** `200 OK`
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "role": "researcher"
  }
}
```

**Errors:**
- `401`: Invalid credentials
- `429`: Too many login attempts (rate limited)

---

### Refresh Token

**POST** `/auth/refresh/`

Get new access token using refresh token.

**Request:**
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response:** `200 OK`
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Errors:**
- `401`: Invalid or expired refresh token

---

### Setup 2FA

**POST** `/auth/2fa/setup/`

Generate TOTP secret for two-factor authentication.

**Response:** `200 OK`
```json
{
  "secret": "JBSWY3DPEBLW64TMMQ======",
  "qr_code_url": "otpauth://totp/HackXHarder:user@example.com?secret=..."
}
```

---

### Verify 2FA

**POST** `/auth/2fa/verify/`

Verify TOTP code and enable 2FA.

**Request:**
```json
{
  "code": "123456"
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "2FA enabled successfully"
}
```

---

### Password Reset Request

**POST** `/auth/password-reset/`

Request password reset email.

**Request:**
```json
{
  "email": "user@example.com"
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Password reset link sent to email"
}
```

---

### Reset Password

**POST** `/auth/password-reset-confirm/`

Reset password with token from email.

**Request:**
```json
{
  "token": "reset-token-from-email",
  "password": "NewPassword123!"
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Password reset successfully"
}
```

---

## Researcher Endpoints

### Get Researcher Profile

**GET** `/researchers/me/`

Get authenticated researcher's profile.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "display_name": "SecurityPro",
  "bio": "Web security researcher",
  "reputation_score": 1250,
  "verified": true,
  "total_submissions": 45,
  "accepted_reports": 38,
  "skill_tags": ["web", "api", "mobile"],
  "wallet_balance": "15500.00",
  "created_at": "2026-01-15T10:30:00Z"
}
```

---

### Update Researcher Profile

**PATCH** `/researchers/me/`

Update profile information.

**Request:**
```json
{
  "display_name": "SecurityProV2",
  "bio": "Senior web security researcher",
  "skill_tags": ["web", "api", "mobile", "cloud"]
}
```

**Response:** `200 OK` (same as GET)

---

### Get Public Researcher Profile

**GET** `/researchers/{researcher_id}/`

View public profile of researcher.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "display_name": "SecurityPro",
  "reputation_score": 1250,
  "verified": true,
  "accepted_reports": 38,
  "created_at": "2026-01-15T10:30:00Z"
}
```

---

### List Researcher Programs

**GET** `/researchers/programs/`

List programs available to researcher.

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Results per page (default: 20)
- `program_type`: Filter by `vdp` or `bbp`
- `status`: Filter by `active`, `paused`, `closed`
- `search`: Search by program title

**Response:** `200 OK`
```json
{
  "count": 150,
  "next": "?page=2",
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "title": "Acme Corp Bug Bounty",
      "company_name": "Acme Corp",
      "program_type": "bbp",
      "status": "active",
      "severity_range": ["critical", "high", "medium"],
      "total_rewards": "250000.00"
    }
  ]
}
```

---

### List Researcher Reports

**GET** `/researchers/reports/`

List all reports submitted by researcher.

**Query Parameters:**
- `page`: Page number
- `limit`: Results per page
- `status`: Filter by report status
- `program_id`: Filter by program

**Response:** `200 OK`
```json
{
  "count": 25,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "program_id": "uuid",
      "program_title": "Acme Corp Bug Bounty",
      "title": "SQL Injection in Search API",
      "status": "validated",
      "severity": "high",
      "submitted_at": "2026-06-20T10:30:00Z",
      "updated_at": "2026-06-23T14:45:00Z"
    }
  ]
}
```

---

### Get Researcher Earnings

**GET** `/researchers/earnings/`

View earnings summary and history.

**Response:** `200 OK`
```json
{
  "total_earned": "45500.00",
  "pending": "5000.00",
  "paid": "40500.00",
  "currency": "USD",
  "summary": {
    "critical": "25000.00",
    "high": "15000.00",
    "medium": "5500.00"
  },
  "recent_payouts": [
    {
      "report_id": "uuid",
      "amount": "5000.00",
      "status": "completed",
      "paid_at": "2026-06-22T10:00:00Z"
    }
  ]
}
```

---

### Get Wallet

**GET** `/researchers/wallet/`

View wallet balance and payment methods.

**Response:** `200 OK`
```json
{
  "balance": "15500.00",
  "currency": "USD",
  "payment_methods": [
    {
      "id": "uuid",
      "type": "bank_transfer",
      "account_name": "John Doe",
      "is_primary": true,
      "verified": true
    }
  ]
}
```

---

## Company Endpoints

### Register Company

**POST** `/companies/register/`

Register new company and company admin account.

**Request:**
```json
{
  "company_name": "Acme Corp",
  "website": "https://acme.com",
  "email": "admin@acme.com",
  "password": "SecurePassword123!",
  "industry": "fintech"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "company_name": "Acme Corp",
  "website": "https://acme.com",
  "verification_status": "pending",
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

### Get Company Profile

**GET** `/companies/me/`

Get authenticated company's profile.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "company_name": "Acme Corp",
  "website": "https://acme.com",
  "verification_status": "verified",
  "logo_url": "https://s3.example.com/logos/acme.png",
  "programs_count": 3,
  "total_reports": 127,
  "avg_resolution_time_days": 8,
  "created_at": "2025-06-01T10:30:00Z"
}
```

---

### Update Company Profile

**PATCH** `/companies/me/`

Update company information.

**Request:**
```json
{
  "company_name": "Acme Corp Updated",
  "website": "https://acme.com",
  "logo_url": "https://s3.example.com/logos/acme-new.png"
}
```

**Response:** `200 OK` (same as GET)

---

### Invite Team Member

**POST** `/companies/me/team/invite/`

Invite user to company team.

**Request:**
```json
{
  "email": "teamlead@acme.com",
  "role": "triage_lead"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "email": "teamlead@acme.com",
  "role": "triage_lead",
  "invitation_sent": true,
  "expires_at": "2026-07-24T10:30:00Z"
}
```

---

### Get Company Analytics

**GET** `/companies/me/analytics/`

View company security program metrics.

**Response:** `200 OK`
```json
{
  "total_reports": 127,
  "open_reports": 8,
  "resolved_reports": 95,
  "avg_resolution_days": 8,
  "total_bounties_paid": "450000.00",
  "monthly_trend": [
    {
      "month": "2026-06",
      "submissions": 15,
      "resolved": 12
    }
  ]
}
```

---

## Program Endpoints

### List Programs

**GET** `/programs/`

Browse publicly available programs.

**Query Parameters:**
- `page`: Page number
- `limit`: Results per page
- `program_type`: Filter by `vdp` or `bbp`
- `status`: Filter by `active`, `paused`, `closed`
- `sort`: Sort by `newest`, `most_active`, `highest_reward`
- `search`: Search by title or company

**Response:** `200 OK`
```json
{
  "count": 350,
  "next": "?page=2",
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "title": "Acme Corp Bug Bounty",
      "company_id": "uuid",
      "company_name": "Acme Corp",
      "program_type": "bbp",
      "status": "active",
      "description": "Help secure our infrastructure",
      "logo_url": "https://s3.example.com/logos/acme.png",
      "created_at": "2025-06-01T10:30:00Z"
    }
  ]
}
```

---

### Get Program Details

**GET** `/programs/{program_id}/`

View complete program information including scope and rewards.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "title": "Acme Corp Bug Bounty",
  "company_id": "uuid",
  "company_name": "Acme Corp",
  "program_type": "bbp",
  "status": "active",
  "visibility": "public",
  "description": "Help secure our infrastructure",
  "rules": "Test only in-scope assets. No denial of service.",
  "safe_harbor_policy": "Researchers authorized under this program...",
  "scope": {
    "in_scope": [
      {
        "id": "uuid",
        "asset_type": "domain",
        "asset_value": "*.acme.com",
        "notes": "All subdomains"
      }
    ],
    "out_of_scope": [
      {
        "id": "uuid",
        "asset_type": "domain",
        "asset_value": "blog.acme.com",
        "notes": "Managed by external vendor"
      }
    ]
  },
  "reward_tiers": [
    {
      "severity": "critical",
      "min_amount": "5000.00",
      "max_amount": "50000.00"
    },
    {
      "severity": "high",
      "min_amount": "2000.00",
      "max_amount": "10000.00"
    }
  ],
  "total_reports": 45,
  "resolved_reports": 38,
  "created_at": "2025-06-01T10:30:00Z"
}
```

---

### Create Program

**POST** `/programs/`

Create new program (company admin only).

**Request:**
```json
{
  "title": "Acme Corp Bug Bounty",
  "program_type": "bbp",
  "description": "Help secure our infrastructure",
  "rules": "Test only in-scope assets...",
  "safe_harbor_policy": "Researchers authorized..."
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "title": "Acme Corp Bug Bounty",
  "status": "draft",
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

### Update Program

**PATCH** `/programs/{program_id}/`

Update program (company admin only).

**Request:**
```json
{
  "title": "Acme Corp Security Program",
  "description": "Updated description"
}
```

**Response:** `200 OK`

---

### Submit Program for Approval

**POST** `/programs/{program_id}/submit-for-approval/`

Move program from draft to pending approval.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "status": "pending_approval",
  "message": "Program submitted for admin review"
}
```

---

### Add Scope

**POST** `/programs/{program_id}/scope/`

Add in-scope or out-of-scope asset.

**Request:**
```json
{
  "asset_type": "domain",
  "asset_value": "*.acme.com",
  "scope": "in_scope",
  "notes": "All subdomains included"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "asset_type": "domain",
  "asset_value": "*.acme.com",
  "scope": "in_scope",
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

### Set Reward Tiers

**POST** `/programs/{program_id}/reward-tiers/`

Define bounty amounts by severity.

**Request:**
```json
{
  "tiers": [
    {
      "severity": "critical",
      "min_amount": "5000.00",
      "max_amount": "50000.00"
    },
    {
      "severity": "high",
      "min_amount": "2000.00",
      "max_amount": "10000.00"
    }
  ]
}
```

**Response:** `200 OK`

---

## Report Endpoints

### Submit Vulnerability Report

**POST** `/reports/`

Submit new vulnerability report (researcher only).

**Request:**
```json
{
  "program_id": "uuid",
  "title": "SQL Injection in Login Form",
  "description": "The login form is vulnerable to SQL injection...",
  "steps_to_reproduce": "1. Go to login page\n2. Enter: admin' OR '1'='1\n3. Click login",
  "affected_asset": "api.acme.com/login",
  "severity": "critical",
  "proof_of_concept": "Attached PoC code demonstrates the issue",
  "vulnerability_type": "sql_injection"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "program_id": "uuid",
  "status": "submitted",
  "submitted_at": "2026-06-24T10:30:00Z"
}
```

**Errors:**
- `400`: Invalid program_id, missing required fields
- `403`: Researcher not enrolled in program
- `429`: Rate limited (20 reports/hour)

---

### List Reports

**GET** `/reports/`

List reports scoped to user role.

**Query Parameters:**
- `page`: Page number
- `limit`: Results per page
- `status`: Filter by report status
- `severity`: Filter by severity level
- `program_id`: Filter by program
- `sort`: Sort by `newest`, `oldest`, `priority`

**Response:** `200 OK`
```json
{
  "count": 127,
  "next": "?page=2",
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "program_id": "uuid",
      "program_title": "Acme Corp Bug Bounty",
      "title": "SQL Injection in Login Form",
      "status": "triaged",
      "severity": "critical",
      "cvss_score": 9.8,
      "submitted_at": "2026-06-20T10:30:00Z",
      "updated_at": "2026-06-23T14:45:00Z"
    }
  ]
}
```

---

### Get Report Details

**GET** `/reports/{report_id}/`

View full report details (object-level permission).

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "program_id": "uuid",
  "program_title": "Acme Corp Bug Bounty",
  "researcher_id": "uuid",
  "researcher_name": "SecurityPro",
  "title": "SQL Injection in Login Form",
  "description": "The login form is vulnerable to SQL injection...",
  "steps_to_reproduce": "1. Go to login page\n2. Enter: admin' OR '1'='1",
  "affected_asset": "api.acme.com/login",
  "vulnerability_type": "sql_injection",
  "status": "triaged",
  "severity": "critical",
  "cvss_score": 9.8,
  "assigned_triage_id": "uuid",
  "submitted_at": "2026-06-20T10:30:00Z",
  "updated_at": "2026-06-23T14:45:00Z",
  "resolved_at": null,
  "comments_count": 5,
  "attachments_count": 2
}
```

---

### Update Report Status

**PATCH** `/reports/{report_id}/status/`

Transition report to new status (allowed transitions only).

**Request:**
```json
{
  "status": "validated",
  "note": "Confirmed as valid critical vulnerability"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "status": "validated",
  "updated_at": "2026-06-24T10:30:00Z"
}
```

**Allowed Transitions:**
- `submitted` → `triaging`, `rejected`
- `triaging` → `validated`, `duplicate`, `rejected`
- `validated` → `resolved`, `rejected`
- `resolved` → `reward_approved`, `closed`
- `reward_approved` → `paid`, `closed`
- `paid` → `closed`

---

### Add Comment

**POST** `/reports/{report_id}/comments/`

Add public or internal comment.

**Request:**
```json
{
  "body": "Can you provide more details about how to reproduce?",
  "is_internal": false
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "author_id": "uuid",
  "author_name": "Security Team",
  "body": "Can you provide more details about how to reproduce?",
  "is_internal": false,
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

### Get Comments

**GET** `/reports/{report_id}/comments/`

List all public comments on report.

**Response:** `200 OK`
```json
{
  "count": 5,
  "results": [
    {
      "id": "uuid",
      "author_name": "Security Team",
      "body": "Can you provide more details?",
      "is_internal": false,
      "created_at": "2026-06-24T10:30:00Z"
    }
  ]
}
```

---

### Upload Attachment

**POST** `/reports/{report_id}/attachments/`

Upload file attachment (multipart/form-data).

**Request:**
```
POST /reports/{report_id}/attachments/
Content-Type: multipart/form-data

file: [binary file data]
description: "PoC exploit code"
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "file_name": "poc.py",
  "file_size_bytes": 2048,
  "content_type": "text/plain",
  "scanned_status": "pending",
  "uploaded_at": "2026-06-24T10:30:00Z"
}
```

**Constraints:**
- Max file size: 100MB
- Allowed types: PDF, PNG, JPG, GIF, TXT, ZIP, RAR

---

### Get Attachments

**GET** `/reports/{report_id}/attachments/`

List report attachments.

**Response:** `200 OK`
```json
{
  "count": 2,
  "results": [
    {
      "id": "uuid",
      "file_name": "poc.py",
      "file_size_bytes": 2048,
      "content_type": "text/plain",
      "scanned_status": "clean",
      "uploaded_at": "2026-06-24T10:30:00Z"
    }
  ]
}
```

---

### Download Attachment

**GET** `/reports/{report_id}/attachments/{attachment_id}/download/`

Download file (signed URL with time limit).

**Response:** `302 Redirect` to signed S3 URL

---

### Get Report History

**GET** `/reports/{report_id}/history/`

View complete status change history.

**Response:** `200 OK`
```json
{
  "count": 8,
  "results": [
    {
      "id": "uuid",
      "from_status": "submitted",
      "to_status": "triaging",
      "changed_by": "Security Team",
      "note": "Report assigned to triage queue",
      "created_at": "2026-06-20T11:00:00Z"
    }
  ]
}
```

---

## Triage Endpoints

### Get Triage Queue

**GET** `/triage/queue/`

List pending reports for triage (triage_lead only).

**Query Parameters:**
- `page`: Page number
- `limit`: Results per page
- `status`: Filter by status
- `severity`: Filter by severity
- `assigned_to`: Filter by assignee

**Response:** `200 OK`
```json
{
  "count": 24,
  "next": "?page=2",
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "title": "SQL Injection in Login",
      "status": "triaging",
      "severity": "critical",
      "submitted_at": "2026-06-24T10:30:00Z",
      "sla_remaining_hours": 36
    }
  ]
}
```

---

### Assign Report

**POST** `/triage/reports/{report_id}/assign/`

Assign report to triage analyst.

**Request:**
```json
{
  "assigned_to_id": "uuid"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "assigned_to_id": "uuid",
  "assigned_at": "2026-06-24T10:30:00Z"
}
```

---

### Set Severity

**PATCH** `/triage/reports/{report_id}/severity/`

Set final severity and CVSS score.

**Request:**
```json
{
  "severity": "critical",
  "cvss_score": 9.8,
  "cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
}
```

**Response:** `200 OK`

---

### Mark Duplicate

**POST** `/triage/reports/{report_id}/mark-duplicate/`

Mark report as duplicate of existing report.

**Request:**
```json
{
  "duplicate_of_id": "uuid",
  "note": "Duplicate of report submitted earlier"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "status": "duplicate",
  "duplicate_of_id": "uuid"
}
```

---

### Recommend Reward

**POST** `/triage/reports/{report_id}/recommend-reward/`

Recommend bounty amount.

**Request:**
```json
{
  "amount": "15000.00",
  "note": "Critical vulnerability with immediate exploit"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "report_id": "uuid",
  "amount": "15000.00",
  "status": "recommended",
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

## Messaging Endpoints

### Get Messages

**GET** `/messages/`

List all messages for authenticated user.

**Query Parameters:**
- `page`: Page number
- `limit`: Results per page
- `unread_only`: Filter unread messages

**Response:** `200 OK`
```json
{
  "count": 42,
  "results": [
    {
      "id": "uuid",
      "conversation_id": "uuid",
      "sender_id": "uuid",
      "sender_name": "Security Team",
      "body": "Please provide additional details...",
      "read": false,
      "created_at": "2026-06-24T10:30:00Z"
    }
  ]
}
```

---

### Send Message

**POST** `/messages/`

Send message in conversation.

**Request:**
```json
{
  "conversation_id": "uuid",
  "body": "Here are the additional details you requested..."
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "conversation_id": "uuid",
  "body": "Here are the additional details...",
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

### Get Conversations

**GET** `/conversations/`

List conversations for authenticated user.

**Response:** `200 OK`
```json
{
  "count": 12,
  "results": [
    {
      "id": "uuid",
      "report_id": "uuid",
      "report_title": "SQL Injection in Login",
      "participants_count": 3,
      "last_message_at": "2026-06-24T10:30:00Z",
      "unread_count": 2
    }
  ]
}
```

---

### Get Conversation Detail

**GET** `/conversations/{conversation_id}/`

View conversation and all messages.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "report_id": "uuid",
  "messages_count": 8,
  "messages": [
    {
      "id": "uuid",
      "sender_name": "Researcher",
      "body": "Initial report submission",
      "created_at": "2026-06-20T10:30:00Z"
    }
  ]
}
```

---

## Payment Endpoints

### Get Wallet

**GET** `/payments/wallet/`

View researcher wallet and balance.

**Response:** `200 OK`
```json
{
  "balance": "15500.00",
  "currency": "USD",
  "pending_rewards": "5000.00",
  "total_earned": "45500.00"
}
```

---

### Get Payment History

**GET** `/payments/history/`

List all payouts and transactions.

**Query Parameters:**
- `page`: Page number
- `status`: Filter by status (pending, completed, failed)

**Response:** `200 OK`
```json
{
  "count": 15,
  "results": [
    {
      "id": "uuid",
      "amount": "5000.00",
      "status": "completed",
      "method": "bank_transfer",
      "paid_at": "2026-06-22T10:00:00Z"
    }
  ]
}
```

---

### Add Payment Method

**POST** `/payments/method/`

Add payout payment method.

**Request:**
```json
{
  "type": "bank_transfer",
  "account_holder": "John Doe",
  "account_number": "1234567890",
  "routing_number": "987654321"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "type": "bank_transfer",
  "account_holder": "John Doe",
  "verified": false,
  "created_at": "2026-06-24T10:30:00Z"
}
```

---

### Approve Bounty

**POST** `/payments/bounties/{report_id}/approve/`

Approve and process bounty (company admin).

**Request:**
```json
{
  "amount": "15000.00"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "report_id": "uuid",
  "amount": "15000.00",
  "status": "approved",
  "approved_at": "2026-06-24T10:30:00Z"
}
```

---

## Admin Endpoints

### List Pending Companies

**GET** `/admin/companies/pending/`

List companies awaiting verification (admin only).

**Response:** `200 OK`
```json
{
  "count": 5,
  "results": [
    {
      "id": "uuid",
      "company_name": "StartupXYZ",
      "website": "https://startupxyz.com",
      "submitted_at": "2026-06-20T10:30:00Z"
    }
  ]
}
```

---

### Approve Company

**POST** `/admin/companies/{company_id}/approve/`

Approve or reject company registration.

**Request:**
```json
{
  "approval": true,
  "note": "Company verified"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "company_name": "StartupXYZ",
  "verification_status": "verified"
}
```

---

### List Pending Programs

**GET** `/admin/programs/pending/`

List programs awaiting approval.

**Response:** `200 OK`
```json
{
  "count": 8,
  "results": [
    {
      "id": "uuid",
      "title": "Company Security Program",
      "company_name": "Company",
      "submitted_at": "2026-06-22T10:30:00Z"
    }
  ]
}
```

---

### Approve Program

**POST** `/admin/programs/{program_id}/approve/`

Approve program for public listing.

**Request:**
```json
{
  "approval": true,
  "note": "Program approved for launch"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "status": "approved",
  "approved_at": "2026-06-24T10:30:00Z"
}
```

---

### List Disputes

**GET** `/admin/disputes/`

List open disputes between researchers and companies.

**Response:** `200 OK`
```json
{
  "count": 3,
  "results": [
    {
      "id": "uuid",
      "report_id": "uuid",
      "dispute_type": "bounty_amount",
      "reported_at": "2026-06-20T10:30:00Z",
      "status": "open"
    }
  ]
}
```

---

### Resolve Dispute

**POST** `/admin/disputes/{dispute_id}/resolve/`

Resolve dispute with admin decision.

**Request:**
```json
{
  "decision": "approve_researcher_claim",
  "note": "Bounty amount increased to requested level"
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "status": "resolved",
  "resolved_at": "2026-06-24T10:30:00Z"
}
```

---

### Get Audit Logs

**GET** `/admin/audit-logs/`

View all platform actions (admin only).

**Query Parameters:**
- `page`: Page number
- `action`: Filter by action type
- `actor_id`: Filter by user
- `target_type`: Filter by model type
- `date_from`: Start date
- `date_to`: End date

**Response:** `200 OK`
```json
{
  "count": 1250,
  "results": [
    {
      "id": "uuid",
      "action": "report.status_changed",
      "actor_name": "Security Team",
      "target_type": "report",
      "target_id": "uuid",
      "metadata": {
        "from_status": "submitted",
        "to_status": "triaging"
      },
      "created_at": "2026-06-24T10:30:00Z"
    }
  ]
}
```

---

## Error Codes

### Standard HTTP Status Codes

| Code | Description |
|------|-------------|
| `200` | OK - Request successful |
| `201` | Created - Resource created successfully |
| `204` | No Content - Successful deletion |
| `400` | Bad Request - Invalid input |
| `401` | Unauthorized - Missing or invalid authentication |
| `403` | Forbidden - Insufficient permissions |
| `404` | Not Found - Resource not found |
| `409` | Conflict - Resource already exists |
| `429` | Too Many Requests - Rate limit exceeded |
| `500` | Internal Server Error - Server error |

### Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input provided",
    "field_errors": {
      "email": ["Invalid email format"],
      "password": ["Password too weak"]
    }
  }
}
```

### Common Error Codes

| Code | Meaning | HTTP Status |
|------|---------|------------|
| `INVALID_CREDENTIALS` | Email or password incorrect | 401 |
| `ACCOUNT_LOCKED` | Account locked after failed attempts | 403 |
| `INSUFFICIENT_PERMISSIONS` | User lacks required role | 403 |
| `RESOURCE_NOT_FOUND` | Resource doesn't exist | 404 |
| `INVALID_TRANSITION` | Report status transition not allowed | 400 |
| `DUPLICATE_EMAIL` | Email already registered | 409 |
| `RATE_LIMITED` | Too many requests | 429 |
| `FILE_TOO_LARGE` | File exceeds size limit | 413 |
| `INVALID_FILE_TYPE` | File type not allowed | 400 |
| `MALWARE_DETECTED` | File flagged as malicious | 400 |

---

## Rate Limiting

All authenticated endpoints are rate-limited. Rate limit headers are included in responses:

**Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1624542600
```

### Rate Limits by Endpoint

| Endpoint | Limit |
|----------|-------|
| `POST /auth/login/` | 5 attempts / 15 minutes per IP |
| `POST /auth/register/` | 10 / hour per IP |
| `POST /reports/` | 20 / hour per user |
| `POST /reports/{id}/comments/` | 60 / hour per user |
| `POST /reports/{id}/attachments/` | 30 / hour per user |
| Other endpoints | 100 / minute per user |

When rate limited, server returns:
```
HTTP/1.1 429 Too Many Requests
Retry-After: 300

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Please try again in 5 minutes.",
    "retry_after": 300
  }
}
```

---

**API Version**: 1.0  
**Last Updated**: 2026-06-24  
**Status**: MVP Ready
