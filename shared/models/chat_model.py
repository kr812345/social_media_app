from datetime import datetime
from shared.utils.db_utils import db

class Chat(db.Model):
    __tablename__ = 'Chat'

    chat_id = db.Column(db.Integer)
    message_id = db.Column(db.Integer,primary_key=True)
    sender_name = db.Column(db.String(50),nullable=False)
    receiver_name = db.Column(db.String(50),nullable=False)
    follower = db.Column(db.Boolean,default=True)
    content = db.Column(db.VARBINARY(255))
    sent_at = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    received_at = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    read_at = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)

class Content(db.Model):
    __tablename__ = 'Content'

    content_id = db.Column(db.Integer,primary_key=True)
    chat_id = db.Column(db.Integer)
    content_type = db.Column(db.String(50))
    content_url = db.Column(db.VARBINARY(255))
    uploaded_at = db.Column(db.DateTime,default=datetime.utcnow)
