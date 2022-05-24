from flask import Blueprint, jsonify, request
from flask_login import login_required
from .validators.signup_validator import signup_validator
from .validators.exception_validator import ValidationException
import json
from ..logic.DAO.Users import Users
from datetime import datetime

user = Blueprint('user', __name__, url_prefix='/user/')

# Sign up -> sign_up
@user.route('/signup', methods=['POST'])
def signup():
    data = request.form.to_dict()
    # validator = signup_validator(data)
    # validator.validate()
    # T = {'birth_date':str(datetime.utcnow().date())}
    # temp = date_validator(T)
    # try:
    #     temp.validate()
    # except ValidationException as en:
    #     return {"status":0, "message":en.message }, 202
    # print("Date validated")

    try:
        validator = signup_validator(data)
        validator.validate()
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202

    data["role_id"] = "user"
    response = Users.add(data)

    if response > 0:
        # Admin registered succesfully
        return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
    else:
        return {"status":0, "message":"Hubo un error interno" }, 400

    # try:
    #     data = json.loads(request.data)

    #     validator = signup_validator(data)
    #     validator.validate()
        
    #     data['status'] = 1
    #     data['role_id'] = 2

    #     # command = RegisterUserCommand(data)
    #     # response = command.execute()

    #     if response > 0:
    #         # Admin registered succesfully
    #         return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
    #     else:
    #         return {"status":0, "message":"Hubo un error interno" }, 400
    # except ValidationException as ex:
    #     return {"status":0, "message":ex.message }, 202
    # except Exception as ex:
    #     traceback.print_exc()
    #     # There was an error adding the admin
    return jsonify(Users.get())
    # return {"status":0, "message":"Hubo un error interno" }, 400




# Sign in -> sign_in/
# get -> user/<username>
# delete -> delete/
# update -> update