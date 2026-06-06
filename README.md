# WebStore_CRM

A comprehensive Customer Relationship Management (CRM) system built with Django and MySQL for managing customer data, sales, and business operations.

## 📋 Project Overview

WebStore_CRM is a web-based application designed to help businesses manage customer relationships, track sales, and streamline operations. It provides a user-friendly interface for managing customer information, interactions, and business metrics.

## 🎯 Key Features

1. **Customer Management** - Store and organize customer information, contact details, and communication history
2. **Sales Tracking** - Monitor sales pipelines, track deals, and manage quotas
3. **Contact Management** - Maintain detailed contact records with multiple communication channels
4. **Dashboard** - Real-time overview of key business metrics and performance indicators
5. **User Authentication** - Secure login system with role-based access control
6. **Data Security** - Environment-based configuration protecting sensitive credentials
7. **MySQL Integration** - Robust MySQL database for reliable data storage and retrieval
8. **Responsive Design** - Mobile-friendly web interface accessible from any device
9. **Admin Panel** - Django admin interface for system management and data administration
10. **Extensible Architecture** - Modular design allowing easy addition of new features and integrations

## 🛠️ Technology Stack

- **Backend**: Django 6.0.5 (Python web framework)
- **Database**: MySQL (with utf8mb4 charset support)
- **Frontend**: Django Templates + HTML/CSS
- **Environment Management**: python-dotenv
- **Server**: WSGI/ASGI compatible

## 📦 Project Structure

```
dcrm/
├── dcrm/                 # Django project settings
│   ├── settings.py       # Configuration (environment-based)
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── website/             # Main Django application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # App URL patterns
│   ├── templates/       # HTML templates
│   ├── admin.py         # Admin interface
│   └── tests.py         # Unit tests
├── manage.py            # Django management utility
├── mydb.py              # Database initialization
├── virt/                # Python virtual environment
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
└── SECURITY_SETUP.md    # Security configuration guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/onesobad/WebStore_CRM.git
cd WebStore_CRM
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Initialize database**
```bash
python mydb.py
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Access the application at `http://localhost:8000`

## 🔐 Security Features

- **Environment Variables**: All sensitive data (credentials, secret keys) stored in `.env`
- **Secure Cookies**: HttpOnly and Secure flags enabled
- **CSRF Protection**: Built-in Django CSRF middleware
- **SQL Injection Prevention**: Django ORM prevents SQL injection attacks
- **XFrame Options**: Clickjacking protection enabled
- **Content Security Policy**: CSP headers configured
- **HSTS Support**: HTTP Strict Transport Security for HTTPS enforcement
- **Password Security**: Django password validation and hashing
- **Debug Control**: Debug mode controlled via environment variable

### Security Setup
For detailed security configuration, see [SECURITY_SETUP.md](./SECURITY_SETUP.md)

## 📚 Documentation

- **Security Guide**: [SECURITY_SETUP.md](./SECURITY_SETUP.md)
- **Django Docs**: https://docs.djangoproject.com/
- **MySQL Docs**: https://dev.mysql.com/doc/

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 📝 Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=tech_db
DB_PORT=3306

# Security (production)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## 🤝 Contributing

1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit pull request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

OneSOBad

## 📧 Support

For support and questions, please create an issue on GitHub.

## 🔄 Version

Current Version: 1.0.0

---

**Last Updated**: June 2024
**Django Version**: 6.0.5
**Python Version**: 3.8+
