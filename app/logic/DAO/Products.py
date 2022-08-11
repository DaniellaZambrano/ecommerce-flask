from .DAO import DAO
from ..models.Product import Product
from app import db

class Products(DAO):
    """
    Product Data Access Object Class.
    """

    def __init__(self):
        pass

    def add(data):
        """ 
        Adds to the Database
        """

        try:
            print("Creating product...")
            product = Product(data["name"], data["sku"], data["price"], data["description"], data["published"], data["seller_id"],data["stock"])
            print("Product created")
            db.session.add(product)
            db.session.commit()
            return product.id

        except Exception as ex:
            print(ex.__repr__())
            return 0

    def get(self):
        """
        Gets all product records from the Database
        """
        products = Product.query.all()
        return products

    def find(product_id):
        """
        Gets a specific product using it ID
        """
        pass

    def get_product(product_id):
        product = Product.query.filter_by(id = product_id).first()

        return product
