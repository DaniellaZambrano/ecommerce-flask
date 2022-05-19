from .BaseModel import BaseModel
from app import db
from .UserType import UserType
from .Email import Email

class User(BaseModel):

    __tablename__ = 'User'

    # Identification Type
    identification_type = db.Column(db.String(1), nullable=False)

    # Identification Number
    identification_number = db.Column(db.String(15), nullable=False, unique=True)
 
    # User Name
    name    = db.Column(db.String(128),  nullable=True)

    # User Lastname
    lastname    = db.Column(db.String(128),  nullable=True)

    # User Cellphone
    cellphone = db.Column(db.String(128),  nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable = False)


    # Identification Data: username, email & password
    username    = db.Column(db.String(128),  nullable=False, unique=True)
    #email    = db.relationship(Email, backref = db.backref('user', uselist = False))
    password = db.Column(db.String(192),  nullable=False)

    # User type to define it permissions
    # user_type = db.relationship(UserType, backref = db.backref('user', lazy=True))

    #Addredd and alternative address
    address = db.Column(db.String(256),  nullable=False,)
    alt_address = db.Column(db.String(256),  nullable=False,)

    # New instance instantiation procedure
    def __init__(self, identification_type, identification_number, cellphone, user_type, name, lastname, username, birth_date, email, passwordm, address, alt_address):

        self.identification_type = identification_type
        self.identification_number = identification_number
        self.name     = name
        self.lastname = lastname
        self.cellphone = cellphone
        self.username = username
        self.birth_date = birth_date
        self.email    = Email(email)
        self.password = passwordm
        self.user_type = UserType(user_type)
        self.address = address
        self.alt_address = alt_address


    def __repr__(self):
        return '<User %r>' % (self.name)

    def is_authenticated(self):
        return True

    def is_active(self):   
        return self.email.confirmed           

    def is_anonymous(self):
        return False  

    def get_id(self):
        return str(self.id)  

    def serialize(self):
        """
        Return as dict
        """        
        return {
            "id": self.id,
            "date_created": self.date_created,
            "name": self.name,
            "lastname": self.lastname,
            "birth_date": self.birth_date,
            "username": self.username,
            "email": self.email.address,
            "user_type": self.user_type.name,
        }
