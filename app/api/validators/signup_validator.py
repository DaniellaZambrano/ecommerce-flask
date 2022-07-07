from cerberus import Validator
from ...logic.models.Email import Email
from ...logic.models.User import User
from .exception_validator import ValidationException
from datetime import datetime

class signup_validator():

    def __init__(self, data):
        self.data = data


    '''
        self.username = username
        self.email    = Email(email)
        self.password = passwordm
        ----------------------------------------------------repeat_password
    '''
    def __translate(self, field):
        translator = {'username':'nombre de usuario',
                    'email':'correo electronico',
                    'password':'contraseña',
                    'repeat_password':'repetir contraseña',
        }

        if translator[field]:
            return translator[field]

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'username': {'type': 'string', 'empty': False, 'required': True},
            'email': {'type': 'string', 'empty': False, 'required': True},
            'password': {'type': 'string', 'empty': False, 'required': True},
            'repeat_password': {'type': 'string', 'empty': False, 'required': True},
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors)[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        if self.data['repeat_password'] != self.data['password']:
            raise ValidationException("La contraseña no coincide")

        if User.query.filter_by(username = self.data['username']).first():
            raise ValidationException("El nombre de usuario ya existe")

        if Email.query.filter_by(address = self.data['email']).first():
            raise ValidationException("El correo electrónico ya existe")
        
        return True
        