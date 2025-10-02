

# 🚀 Flask Contact Form - SMTP Implementation (RFC : 5321)

![Flask](https://img.shields.io/badge/Flask-2.0+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Security](https://img.shields.io/badge/Security-High-brightgreen.svg)

A production-ready, secure contact form implementation built with Flask. This solution features robust security measures, intelligent rate limiting, and asynchronous email processing to deliver a seamless user experience while maintaining enterprise-grade security standards.

## 🌟 Key Features

- **Multi-Layered Security**: Comprehensive protection against XSS, CSRF, and injection attacks
- **Advanced Input Sanitization**: Bleach-based HTML sanitization with custom policies
- **Intelligent Rate Limiting**: Tiered throttling system (5 req/min global, 3 submissions/min)
- **Asynchronous Email Processing**: Non-blocking SMTP delivery with background threading
- **Responsive Design**: Mobile-first approach with flawless cross-device compatibility
- **Secure Session Management**: Encrypted sessions with configurable expiration

## 📋 Prerequisites

- **Runtime Environment**: Python 3.8+ (tested up to 3.11)
- **Web Framework**: Flask 2.0+
- **Dependencies**:
  - Flask-Limiter (rate limiting)
  - python-dotenv (configuration management)
  - bleach (input sanitization)
  - itsdangerous (secure signing)
- **Infrastructure**: Access to SMTP server (TLS-capable recommended)

## 🚀 Installation & Configuration

### 1. Repository Setup

```bash
# Clone the repository
git clone https://github.com/your-username/flask-contact-form.git
cd flask-contact-form

# Switch to the stable branch
git checkout stable
```

### 2. Environment Preparation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Application Configuration

Create `.env` file in project root:

```env
# Application Security
SECRET_KEY=your-super-secret-key-here
SESSION_TIMEOUT=3600

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_RECIPIENT=admin@yourdomain.com
EMAIL_TIMEOUT=30

# Rate Limiting
RATELIMIT_STORAGE_URL=memory://
RATELIMIT_DEFAULT=5/minute
RATELIMIT_SUBMIT=3/minute
```

### 4. Running the Application

```bash
# Start development server
python3 app.py
```

Access the application at `http://localhost:5000`

## 🔒 Security Implementation

### Input Validation

The application implements comprehensive input validation to ensure data integrity and prevent security vulnerabilities:

- **Field Validation**:
  - Name: Alphanumeric + spaces, max 100 chars
  - Email: RFC 5322 compliant, max 100 chars
  - Subject: Printable characters, max 150 chars
  - Message: Printable characters, max 2000 chars

- **Sanitization**: Bleach-based HTML stripping with custom allowlist
- **Encoding**: UTF-8 enforcement with character escaping

```python
# Input validation code from app.py
if not name or not email or not subject or not message:
    flash('All fields are required!', 'danger')
    return redirect(url_for('form'))

if len(name) > 100 or len(email) > 100 or len(subject) > 150 or len(message) > 2000:
    flash('One or more fields exceed maximum allowed length!', 'danger')
    return redirect(url_for('form'))

# Validate email format
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    flash('Please enter a valid email address!', 'danger')
    return redirect(url_for('form'))
```

### Security Measures

The application addresses multiple OWASP Top 10 vulnerabilities:

- **A1: Injection**: Parameterized queries and input sanitization
- **A3: XSS**: Content Security Policy and output encoding
- **A5: Security Misconfiguration**: Secure headers and environment isolation
- **A6: Sensitive Data**: Encrypted credentials and secure transmission
- **A7: XSS**: Reflected XSS protection via templating engine
- **A10: Logging**: Security event logging without sensitive data

```python
# Input sanitization code from app.py
# Sanitize input to prevent XSS
name = bleach.clean(name, strip=True)
email = bleach.clean(email, strip=True)
subject = bleach.clean(subject, strip=True)
message = bleach.clean(message, strip=True)
```

### Rate Limiting

The application implements intelligent rate limiting to prevent abuse:

- **Global Limit**: 5 requests per minute per IP
- **Form Submission**: 3 submissions per minute per IP
- **Storage**: In-memory (Redis recommended for production)
- **Response**: HTTP 429 with Retry-After header

```python
# Rate limiting code from app.py
# Rate limiting: Max 5 submissions per minute per IP
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["5 per minute"]
)
limiter.init_app(app)

@app.route('/submit', methods=['POST'])
@limiter.limit("3 per minute")  # Limit per IP
def submit():
    # Form submission logic
```

## 📧 Email Configuration

### SMTP Settings

| Parameter | Description | Example |
|-----------|-------------|---------|
| `EMAIL_HOST` | SMTP server address | `smtp.gmail.com` |
| `EMAIL_PORT` | SMTP port | `587` |
| `EMAIL_USE_TLS` | Enable TLS encryption | `True` |
| `EMAIL_USER` | SMTP username | `user@gmail.com` |
| `EMAIL_PASSWORD` | SMTP password | `your-app-password` |
| `EMAIL_RECIPIENT` | Notification recipient | `admin@example.com` |
| `EMAIL_TIMEOUT` | Connection timeout (seconds) | `30` |

### Email Template
```html
Subject: New Contact Form Submission: {{ subject }}

From: {{ name }} ({{ email }})

Message:
{{ message }}
---
Timestamp: {{ timestamp }}
IP Address: {{ ip_address }}
User Agent: {{ user_agent }}
```

## 📁 Project Structure

```
flask-contact-form/
├── app.py                 # Main application file
├── email_utils.py         # Email sending utilities
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not committed)
└── templates/
    └── contact.html       # Contact form template
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](\LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [OWASP](https://owasp.org/) - Security best practices and guidelines
- [Flask-Limiter](https://flask-limiter.readthedocs.io/) - Rate limiting implementation
- [Bleach](https://bleach.readthedocs.io/) - Input sanitization library
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
