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
    msg = request.form.get('query-input')
    new_contact = contact(name=name, message=msg)
    db.session.add(new_contact)
    db.session.commit()
    return f"<h1>Thank you {name}!</h1><p>Your message has been saved.</p>"

@app.route('/admin')
def admin():
    all_messages = contact.query.all()
    return render_template('admin.html', messages=all_messages)

if __name__ =='__main__':
   import os
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
   