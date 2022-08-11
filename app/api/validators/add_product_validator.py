from cerberus import Validator
from ...logic.models.Product import Product
from .exception_validator import ValidationException

class add_product_validator():

    '''
        self.name = name
        self.sku = sku
        self.price = price
        self.description = description
        self.published = published
        self.seller_id = seller_id
        self.stock = stock

    '''

    def __init__(self, data):
        self.data = data

    def __translate(self, field):
        translator = {'name':'nombre',
                    'sku':'identificador unico',
                    'price':'precio',
                    'description':'descripcion',
                    'published':'esta_publicado',
                    'seller_id':'ID del vendedor',
                    'stock':'inventario',
        }

        if translator[field]:
            return translator[field]

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'name': {'type': 'string', 'nullable': False},
            'sku': {'type': 'string','empty': False, 'required': True, 'nullable': False},
            'price': {'type': 'float','empty': False, 'required': True},
            'description': {'type': 'string','empty': False, 'required': True},
            'seller_id': {'type': 'integer','empty': False, 'required': True,'coerce':is_numeric()},
            'stock': {'type': 'integer','empty': False, 'required': True,'coerce':is_numeric()}
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors)[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        # Check sku, stock, price
        

def is_numeric(s):
    try:
        number = s.isnumeric()
    except:
        print("Error on integer conversion")
    return number
