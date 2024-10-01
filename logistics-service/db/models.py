from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(80), nullable=False)
#     item = db.Column(db.String(120), nullable=False)
#     status = db.Column(db.String(20), nullable=False)
