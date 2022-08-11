from cerberus import Validator
from ...logic.models.Email import Email
from ...logic.models.User import User
from .exception_validator import ValidationException
from datetime import datetime

class signup_validator():

    def __init__(self, data):
        self.data = data


    '''
        self.identification_type = identification_type
        self.identification_number = identification_number
        self.name     = name
        self.lastname = lastname
        self.cellphone = cellphone
        self.username = username
        self.birth_date = birth_date
        self.email    = Email(email)
        self.password = passwordm
        ----------------------------------------------------repeat_password
        self.address = address

    '''
    def __translate(self, field):
        translator = {'name':'nombre',
                    'last_name':'apellido',
                    'identification_type':'tipo de documento',
                    'identification_number':'número de identidad',
                    'password':'contraseña',
                    'repeat_password':'repetir contraseña',
                    'cellphone':'teléfono',
                    'username':'nombre de usuario',
                    'email':'correo electronico',
                    'birth_date':'fecha de nacimiento',
                    'address':'Direccion',
                    'alt_address':'Direccion alterna'
        }

        if translator[field]:
            return translator[field]

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'identification_type': {'type': 'string', 'empty': False, 'required': True},
            'identification_number': {'type': 'string', 'empty': False, 'required': True},
            'name': {'type': 'string', 'nullable': True},
            'last_name': {'type': 'string', 'nullable': True},
            'cellphone': {'type': 'string', 'empty': False, 'required': True},
            'birth_date':{'type':'date', 'nullable': False, 'coerce':to_date},
            'username': {'type': 'string', 'empty': False, 'required': True},
            'email': {'type': 'string', 'empty': False, 'required': True},
            'password': {'type': 'string', 'empty': False, 'required': True},
            'repeat_password': {'type': 'string', 'empty': False, 'required': True},
            'address': {'type': 'string', 'empty': False, 'required': True},
            'alt_address': {'type': 'string', 'required': False}
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors)[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        if self.data['repeat_password'] != self.data['password']:
            raise ValidationException("La contraseña no coincide")

        if User.query.filter_by(username = self.data['username']).first():
            raise ValidationException("El nombre de usuario ya existe")

        if User.query.filter_by(cellphone = self.data['cellphone']).first():
            raise ValidationException("Ya existe un usuario con ese teléfono")

        if Email.query.filter_by(address = self.data['email']).first():
            raise ValidationException("El correo electrónico ya existe")

        if User.query.filter_by(identification_number = self.data['identification_number']).first():
            raise ValidationException("Ya existe un usuario con ese número de identificación")
        
        return True

def to_date(s):
    try:
        date = datetime.strptime(s,"%Y-%m-%d").date()
    except:
        print("Error on date conversion")
    return date
