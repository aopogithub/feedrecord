from flask_sqlalchemy import SQLAlchemy
from app import db

#db = SQLAlchemy()

class FeedingRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feeding_type = db.Column(db.String(10), nullable=False)  # 'breast' or 'bottle'
    amount = db.Column(db.Float, nullable=False)  # Amount in ml
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    notes = db.Column(db.String(200))  # 添加 notes 字段
    
    def __repr__(self):
        return f'<FeedingRecord {self.id}: {self.feeding_type} - {self.amount}ml>'