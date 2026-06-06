# Security Setup Guide for WebStore_CRM

## Overview
This project has been updated with security best practices including environment-based configuration and hardened security settings.

## Setup Instructions

### 1. Environment Variables Setup

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` with your actual configuration:
```env
# Django
SECRET_KEY=<generate-with-python-secrets-module>
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<your-password>
DB_NAME=tech_db
DB_PORT=3306

# Security (for production)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

### 2. Generate SECRET_KEY

Run in Python shell:
```python
import secrets
print(secrets.token_urlsafe(50))
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Create database
python mydb.py

# Apply migrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

## Security Improvements Made

### ✅ Database Credentials
- **Before**: Hardcoded credentials in `settings.py` and `mydb.py`
- **After**: Environment variables via `.env` file

### ✅ Django Secret Key
- **Before**: Insecure key in settings
- **After**: Environment variable (must be changed for production)

### ✅ Debug Mode
- **Before**: `DEBUG = True` always
- **After**: Controlled via `DEBUG` environment variable (defaults to `False`)

### ✅ ALLOWED_HOSTS
- **Before**: Empty list (security issue)
- **After**: Configured via environment variable with sensible defaults

### ✅ SSL/HTTPS Settings
- Security headers enabled
- HSTS support for HTTPS enforcement
- Secure cookie settings for production

### ✅ File Protection
- `.gitignore` prevents accidentally committing `.env`, logs, and sensitive files
- `.env` **must never be committed** to version control

### ✅ Logging
- Added comprehensive logging configuration
- Logs directory created automatically
- Log level configurable via environment

## Production Deployment Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Generate a strong `SECRET_KEY` using `secrets.token_urlsafe(50)`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set database credentials with strong passwords
- [ ] Enable HTTPS/SSL settings:
  - `SECURE_SSL_REDIRECT=True`
  - `SESSION_COOKIE_SECURE=True`
  - `CSRF_COOKIE_SECURE=True`
  - `SECURE_HSTS_SECONDS=31536000` (1 year)
- [ ] Run `python manage.py check --deploy`
- [ ] Set up proper logging and monitoring

## Files Modified

- `dcrm/settings.py` - Environment-based configuration
- `mydb.py` - Environment variables for database creation
- `.env.example` - Template for environment variables
- `.gitignore` - Protection for sensitive files

## Never Commit

- `.env` (always use `.env.example` as template)
- Database files (`*.db`, `*.sqlite*`)
- Log files in `logs/` directory
- Virtual environment files in `venv/`

## Reference

- [Django Security Docs](https://docs.djangoproject.com/en/6.0/topics/security/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
