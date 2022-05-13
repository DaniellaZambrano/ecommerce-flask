from flask import Blueprint, request
from flask_login import login_required
from .validators.signup_validator import signup_validator 
import json
from ..logic.DAO.Users import Users

user = Blueprint('user', __name__, url_prefix='/user/')

# Sign up -> sign_up
@user.route('/signup', methods=['POST'])
def signup():
    print(request.form)

    data = request.form.to_dict()
    validator = signup_validator(data)
    validator.validate()

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