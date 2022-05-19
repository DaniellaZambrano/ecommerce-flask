from .BaseModel import BaseModel
from app import db
from sqlalchemy.orm import backref

class Email(BaseModel):

    __tablename__ = 'Email'

    address = db.Column(db.String(64), nullable=False, unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', backref=backref('Email', uselist=False))


    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return '<Email %r>' % (self.address)

    def confirm_email(self,confirmation):
        self.confirmed = confirmation

    def serialize(self):
        """
        Return the info as dictionary
        """
        return {
            "Email": self.address,
            "Confirmed": self.confirmed
        }