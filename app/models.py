from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FeedingRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feeding_type = db.Column(db.String(10), nullable=False)  # 'breast' or 'bottle'
    amount = db.Column(db.Float, nullable=False)  # Amount in ml
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<FeedingRecord {self.id}: {self.feeding_type} - {self.amount}ml>'