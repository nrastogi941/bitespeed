from datetime import datetime
from src.databases import db

class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(20))
    email = db.Column(db.String(50))
    linkedId = db.Column(db.Integer)
    linkPrecedence = db.Column(db.Enum("primary", "secondary"), default="primary")
    createdAt = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deletedAt = db.Column(db.DateTime, nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)
    
    def update(self, obj_in):
        for key, value in obj_in.items():
            setattr(self, key, value)
