from cerberus import Validator
from ...logic.models.Email import Email as ExistingEmails
from ...logic.models.User import User
from .exception_validator import ValidationException

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
        if field == 'name':
            return 'nombre'

        if field == 'lastname':
            return 'apellido'

        if field == 'identification_type':
            return 'tipo de documento'

        if field == 'identification_number':
            return 'número de identidad'

        if field == 'password':
            return 'contraseña'

        if field == 'repeat_password':
            return 'repetir contraseña'

        if field == 'cellphone':
            return 'teléfono'

        if field == 'username':
            return 'nombre de usuario'

        if field == 'email':
            return 'correo electrónico'

        if field == 'birth_date':
            return 'fecha de nacimiento'

        if field == 'address':
            return 'Direccion'

        return field

    to_date = lambda s: datetime.strptime(s, '%Y-%m-%d')

    def check_email(field, value, error):
        if ExistingEmails.query.filter_by(address = value).first() != None:
            error(field,'Correo ya en uso')            

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'identification_type': {'type': 'string', 'empty': False, 'required': True},
            'identification_number': {'type': 'string', 'empty': False, 'required': True},
            'name': {'type': 'string', 'nullable': True},
            'lastname': {'type': 'string', 'nullable': True},
            'cellphone': {'type': 'string', 'empty': False, 'required': True},
            # 'birth_date':{'type':'datetime', 'nullable': False,'coerce':self.to_date},
            'username': {'type': 'string', 'empty': False, 'required': True},
            # 'email': {'type': 'Email', 'empty': False, 'required': True, 'check_with':self.check_email},
            'password': {'type': 'string', 'empty': False, 'required': True},
            'repeat_password': {'type': 'string', 'empty': False, 'required': True},
            'address': {'type': 'string', 'empty': False, 'required': True}
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors.keys())[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        if self.data['repeat_password'] != self.data['password']:
            raise ValidationException("La contraseña no coincide")

        if User.query.filter_by(username = self.data['username']).first():
            raise ValidationException("El nombre de usuario ya existe")

        if User.query.filter_by(cellphone = self.data['cellphone']).first():
            raise ValidationException("Ya existe un usuario con ese teléfono")

        # if User.query.filter_by(email = self.data['email']).first():
        #     raise ValidationException("El correo electrónico ya existe")

        if User.query.filter_by(identification_number = self.data['identification_number']).first():
            raise ValidationException("Ya existe un usuario con ese número de identificación")
