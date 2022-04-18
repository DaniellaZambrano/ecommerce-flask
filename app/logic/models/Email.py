from .BaseModel import BaseModel
from app import db

class Email(BaseModel):

    __tablename__ = 'Email'

    def __init__(self, address):
        self.address = address
        self.confirmed = False

    def __repr__(self):
        return '<Email %r>' % (self.address)

    def serialize(self):
        """
        Return the info as dictionary
        """
        return {
            "Email": self.address,
            "Confirmed": self.confirmed
        }