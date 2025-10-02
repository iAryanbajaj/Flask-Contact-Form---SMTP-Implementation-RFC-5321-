# email_utils.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

def send_email(name, email, subject, message):
    """Send professional HTML feedback email to admin"""
    smtp_config = {
        'server': os.environ.get('SMTP_SERVER'),
        'port': int(os.environ.get('SMTP_PORT', 587)),
        'username': os.environ.get('SMTP_USERNAME'),
        'password': os.environ.get('SMTP_PASSWORD'),
        'recipient': os.environ.get('TO_EMAIL')
    }

    if not all(smtp_config.values()):
        raise ValueError("Missing SMTP configuration. Check environment variables.")

    msg = MIMEMultipart('alternative')
    msg['From'] = f"Feedback System <{smtp_config['username']}>"
    msg['To'] = smtp_config['recipient']
    msg['Subject'] = f"New Feedback: {subject}"
    msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

    # Professional HTML Template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Feedback Notification</title>
        <style>
            /* Email Client Reset */
            body, table, td, a {{ 
                -webkit-text-size-adjust: 100%; 
                -ms-text-size-adjust: 100%; 
            }}
            table, td {{ 
                mso-table-lspace: 0pt; 
                mso-table-rspace: 0pt; 
            }}
            img {{ 
                -ms-interpolation-mode: bicubic; 
                border: 0; 
                height: auto; 
                line-height: 100%; 
                outline: none; 
                text-decoration: none; 
            }}
            table {{ 
                border-collapse: collapse !important; 
            }}
            body {{ 
                height: 100% !important; 
                margin: 0 !important; 
                padding: 0 !important; 
                width: 100% !important; 
            }}

            /* Typography */
            body {{
                font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
                font-size: 16px;
                line-height: 1.6;
                color: #333;
                background-color: #f5f7fa;
                margin: 0;
                padding: 20px;
            }}

            /* Layout */
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            }}

            /* Header */
            .header {{
                background: linear-gradient(135deg, #1a73e8, #185abc);
                padding: 30px;
                text-align: center;
                color: white;
            }}
            .header h1 {{
                margin: 0;
                font-size: 24px;
                font-weight: 600;
                letter-spacing: -0.5px;
            }}
            .header p {{
                margin: 8px 0 0;
                font-size: 14px;
                opacity: 0.9;
            }}
            .header .icon {{
                font-size: 48px;
                margin-bottom: 15px;
                opacity: 0.9;
            }}

            /* Content */
            .content {{
                padding: 30px;
            }}
            .info-section {{
                margin-bottom: 25px;
            }}
            .info-item {{
                display: flex;
                align-items: flex-start;
                margin-bottom: 12px;
            }}
            .info-label {{
                font-weight: 600;
                color: #5f6368;
                min-width: 80px;
                margin-right: 15px;
            }}
            .info-value {{
                flex: 1;
                color: #202124;
            }}

            /* Message Box */
            .message-box {{
                background-color: #f8f9fa;
                border-left: 4px solid #1a73e8;
                border-radius: 4px;
                padding: 20px;
                margin-top: 25px;
            }}
            .message-title {{
                font-size: 16px;
                font-weight: 600;
                margin: 0 0 12px;
                color: #1a73e8;
            }}
            .message-content {{
                white-space: pre-wrap;
                color: #3c4043;
                margin: 0;
            }}

            /* Divider */
            .divider {{
                height: 1px;
                background-color: #e8eaed;
                margin: 25px 0;
            }}

            /* Footer */
            .footer {{
                background-color: #f8f9fa;
                padding: 20px;
                text-align: center;
                font-size: 13px;
                color: #5f6368;
                border-top: 1px solid #e8eaed;
            }}
            .footer p {{
                margin: 0 0 8px;
            }}
            .footer a {{
                color: #1a73e8;
                text-decoration: none;
            }}
            .footer a:hover {{
                text-decoration: underline;
            }}

            /* Responsive */
            @media only screen and (max-width: 600px) {{
                .container {{
                    width: 100% !important;
                    border-radius: 0 !important;
                }}
                .header {{
                    padding: 20px !important;
                }}
                .content {{
                    padding: 20px !important;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header Section -->
            <div class="header">
                <div class="icon">✉️</div>
                <h1>New Feedback Received</h1>
                <p>Customer Feedback System</p>
            </div>
            
            <!-- Content Section -->
            <div class="content">
                <!-- Sender Information -->
                <div class="info-section">
                    <div class="info-item">
                        <div class="info-label">From:</div>
                        <div class="info-value">{name} &lt;{email}&gt;</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Subject:</div>
                        <div class="info-value">{subject}</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Received:</div>
                        <div class="info-value">{datetime.now().strftime("%B %d, %Y at %I:%M %p")}</div>
                    </div>
                </div>
                
                <div class="divider"></div>
                
                <!-- Message Section -->
                <div class="message-box">
                    <h3 class="message-title">Feedback Message</h3>
                    <p class="message-content">{message}</p>
                </div>
            </div>
            
            <!-- Footer Section -->
            <div class="footer">
                <p>This is an automated notification from your feedback system.</p>
                <p>© {datetime.now().year} Your Company Name. All rights reserved.</p>
                <p>
                    <a href="#">Privacy Policy</a> | 
                    <a href="#">Terms of Service</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    # Plain text alternative
    text_template = f"""
    NEW FEEDBACK RECEIVED
    
    From: {name} <{email}>
    Subject: {subject}
    Received: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
    
    FEEDBACK MESSAGE:
    {message}
    
    ---
    This is an automated notification from your feedback system.
    © {datetime.now().year} Your Company Name. All rights reserved.
    """

    msg.attach(MIMEText(text_template, 'plain'))
    msg.attach(MIMEText(html_template, 'html'))

    try:
        with smtplib.SMTP(smtp_config['server'], smtp_config['port']) as server:
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_config['username'], smtp_config['password'])
            server.send_message(msg)
        print("✅ Feedback email sent to admin successfully!")
    except Exception as e:
        print(f"❌ SMTP Error (admin email): {str(e)}")
        raise Exception(f"SMTP Error (admin email): {str(e)}")