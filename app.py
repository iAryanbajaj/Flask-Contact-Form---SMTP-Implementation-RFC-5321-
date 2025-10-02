from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re
from email_utils import send_email
import threading
import bleach  # for sanitizing user input

# Load environment variables
load_dotenv(".env")

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Rate limiting: Max 5 submissions per minute per IP
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["5 per minute"]
)
limiter.init_app(app)

# Async email sender
def send_email_async(name, email, subject, message):
    threading.Thread(target=send_email, args=(name, email, subject, message)).start()

@app.route('/')
def form():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
@limiter.limit("3 per minute")  # Limit per IP
def submit():
    # Get form data
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()

    # Sanitize input to prevent XSS
    name = bleach.clean(name, strip=True)
    email = bleach.clean(email, strip=True)
    subject = bleach.clean(subject, strip=True)
    message = bleach.clean(message, strip=True)

    # Input validation
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

    # Flash success immediately
    flash('Your feedback has been submitted successfully!', 'success')

    # Send email asynchronously
    send_email_async(name, email, subject, message)

    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
