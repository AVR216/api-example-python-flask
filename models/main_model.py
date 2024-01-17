# models/hello_model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hello(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
