from cerberus import Validator
from ...logic.models.Email import Email
from ...logic.models.User import User
from .exception_validator import ValidationException
from datetime import datetime

class date_validator():

    def __init__(self, data):
        self.data = data


    def __translate(self, field):
        if field == 'birth_date':
            return 'fecha de nacimiento'
        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {'birth_date':{'type':'date', 'coerce':to_date}}

        v = Validator()
        v.schema = schema
        if not v.validate(self.data):
            field = list(v.errors)[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        return True


def to_date(s):
    try:
        date = datetime.strptime(s,"%Y-%m-%d").date()
    except:
        print("Error on date conversion")
    return date
