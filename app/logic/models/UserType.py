from .BaseModel import BaseModel
from app import db
from sqlalchemy.orm import backref

class UserType(BaseModel):

    __tablename__ = 'UserType'

    # Role name or type
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', backref=backref('UserType'))

    # New instance instantiation procedure
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<UserType %r>' % (self.name)

    def serialize(self):
        """
        Return the info as dictionary
        """
        return {
            "id": self.id,
            "name": self.name
        }