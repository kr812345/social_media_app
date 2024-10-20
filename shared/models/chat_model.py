from datetime import datetime
from shared.utils.db_utils import db

class Chat(db.Model):
    __tablename__ = 'Chat'

    id = db.Column(db.String(10) , primary_key=True)
    sender_name = db.Column(db.Integer, unique=True,nullable=False)
    receiver_name = db.Column(db.Integer, unique=True,nullable=False)
    follower = db.Column(db.Boolean,default=False)
    content_type = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text)
    sent_at = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    received_at = db.Column(db.DateTime,nullable=False)
    read_at = db.Column(db.DateTime,nullable=False)


class Content(db.Model):
    __tablename__ = 'Content'

    content_id = db.Column(db.Integer, primary_key=True)
    content_type = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    