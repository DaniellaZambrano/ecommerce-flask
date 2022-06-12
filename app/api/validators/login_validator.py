from cerberus import Validator
from ...logic.models.Email import Email
from ...logic.models.User import User
from .exception_validator import ValidationException
from datetime import datetime
import bcrypt

class login_validator():

    def __init__(self, data):
        self.data = data


    '''
        self.username = username
        self.password = password
    '''
    def __translate(self, field):
        translator = {
                    'username':'nombre de usuario o correo electronico',
                    'password':'contraseña',
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
            'password': {'type': 'string', 'empty': False, 'required': True},
            'remember_me': {'type': 'boolean', 'empty': False, 'required': True},
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors)[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        # if self.data['repeat_password'] != self.data['password']:
        #     raise ValidationException("La contraseña no coincide")

        username = self.data["username"]

        username_exists = User.query.filter_by(username = username).first()
        email_exists = Email.query.filter_by(address = username).first()

        if not username_exists and not email_exists:
            raise ValidationException("Los datos de usuario no estan registrados")

        if email_exists is not None: print("email_id:{}".format(email_exists.id))
        if username_exists is not None: print("user:{}".format(username_exists))


        user = username_exists if username_exists else User.query.filter_by(id = email_exists.id).first()

        if user is None:
            raise ValidationException("Error")

        if not bcrypt.checkpw(bytes(self.data["password"],'utf-8'), bytes(user.password, 'utf-8')):
            raise ValidationException("Contrasena invalida")

        return user
