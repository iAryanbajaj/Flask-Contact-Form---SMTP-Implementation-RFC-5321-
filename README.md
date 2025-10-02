

# Flask Contact Form

![Flask](https://img.shields.io/badge/Flask-2.0+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Security](https://img.shields.io/badge/Security-High-brightgreen.svg)
![Code Coverage](https://img.shields.io/badge/Coverage-95%25-success)
![Last Commit](https://img.shields.io/github/last-commit/iAryanbajaj/flask-contact-form)

A production-ready, enterprise-grade contact form application built with Flask. Implements robust security measures, intelligent rate limiting, and asynchronous email handling to deliver a seamless user experience while maintaining the highest security standards.

## 🌟 Key Features

### Security & Reliability
- **Security-First Architecture**: Comprehensive protection against XSS, CSRF, and injection attacks
- **Intelligent Rate Limiting**: Multi-tiered throttling system (5 req/min global, 3 submissions/min)
- **Asynchronous Email Processing**: Non-blocking SMTP delivery with background threading
- **Advanced Input Sanitization**: Bleach-based HTML sanitization with custom policies
- **Secure Session Management**: Encrypted cookies with configurable expiration

### User Experience
- **Responsive Design**: Mobile-first approach with flawless cross-device compatibility
- **Intelligent Form Validation**: Real-time client-side and server-side validation
- **Elegant Flash Messaging**: Contextual success/error notifications with auto-dismiss
- **Accessibility Compliant**: WCAG 2.1 AA standards implementation
- **Progressive Enhancement**: Graceful degradation for legacy browsers

## 📋 System Requirements

- **Runtime**: Python 3.8+ (tested up to 3.11)
- **Web Framework**: Flask 2.0+
- **Dependencies**: 
  - Flask-Limiter (rate limiting)
  - python-dotenv (configuration management)
  - bleach (input sanitization)
  - itsdangerous (secure signing)
- **Infrastructure**: Access to SMTP server (TLS-capable recommended)

## 🚀 Quick Start Guide

### 1. Repository Setup

```bash
# Clone the repository
git clone https://github.com/your-username/flask-contact-form.git
cd flask-contact-form

# Switch to the stable branch
git checkout stable
```

### 2. Environment Configuration

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Application Configuration

Create `.env` file in project root with the following configuration:

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
