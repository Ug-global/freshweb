import smtplib
from email.mime.text import MIMEText

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site_data.db'
db = SQLAlchemy(app)

# Tabe to store contact messages
class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    # creat the database file
    with app.app_context():
         db.create_all()
         print("Database tables created successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit():
    name = request.form.get('name-input')
    msg_content = request.form.get('query-input')
    # We use a dummy email since your current form only asks for Name and Message
    email = "Website Visitor"

    # 1. Save to Database (Keeping your existing logic)
    new_contact = contact(name=name, message=msg_content)
    db.session.add(new_contact)
    db.session.commit()

    # 2. EMAIL NOTIFICATION LOGIC
    sender_email = "ugochukwuonyebuchi111@gmail.com"
    # PASTE YOUR 16-DIGIT CODE BELOW (Remove any spaces)
    app_password = "kfkpxosbwimqekqv"

    subject = f"🚀 New Client Lead: {name}"
    body = f"Ugo, you have a new message!\n\nName: {name}\nMessage: {msg_content}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = sender_email # Sending to yourself

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, sender_email, msg.as_string())
    except Exception as e:
        print(f"Email error: {e}")

    return f"<h1>Thank you {name}!</h1><p>Your message has been saved and I've been notified.</p>"

@app.route('/admin/<secret_key>')
def admin(secret_key):
    # CHOOSE YOUR OWN SECRET PASSWORD HERE
    my_password = "ugo_global_2026"

    if secret_key == my_password:
        all_messages = contact.query.all()
        return render_template('admin.html', messages=all_messages)
    else:
        return "<h1>Access Denied</h1><p>You do not have permission to view this page.</p>", 403



if __name__ =='__main__':
   import os
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
