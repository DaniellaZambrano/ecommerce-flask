from .BaseModel import BaseModel
from .User import User
from app import db
from sqlalchemy.orm import backref

class Product(BaseModel):

    __tablename__ = 'Product'

    # Product name
    name = db.Column(db.String(128), nullable=False)

    # Product SKU
    sku = db.Column(db.String(128), nullable=False)

    # Product price
    price = db.Column(db.Integer,  nullable=False)

    # Product description
    description = db.Column(db.String(200),  nullable=False)

    # Product is published or not
    published = db.Column(db.Boolean,  nullable=False)

    # category = db.relationship('Categories', backref = db.backref('Item', lazy=True))

    # Product publication owner / Product seller
    seller_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    seller = db.relationship('User', backref=backref('Product', uselist=False))

    # Product stock
    stock = db.Column(db.Integer, nullable=False)


    def __init__(self, name, sku, price, description, published, seller_id,stock):
        self.name = name
        self.sku = sku
        self.price = price
        self.description = description
        self.published = published
        self.seller_id = seller_id
        self.seller = User.query.filter_by(id = seller_id).first()
        self.stock = stock

    def __repr__(self):
        return '<Product %r>' % (self.id)