from flask import Blueprint, jsonify, request
from flask_login import login_required, login_user
from .validators.signup_validator import signup_validator
from .validators.login_validator import login_validator
from .validators.exception_validator import ValidationException
import json
from ..logic.DAO.Users import Users
from datetime import datetime

user = Blueprint('user', __name__, url_prefix='/user/')

# Sign up -> sign_up
@user.route('/signup', methods=['POST'])
def signup():

    data = request.form.to_dict()

    try:
        validator = signup_validator(data)
        validator.validate()
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202

    data["role_id"] = "user"
    response = Users.add(data)

    if response > 0:
        # User registered succesfully
        return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
    else:
        return {"status":0, "message":"Hubo un error interno" }, 400



# Sign in -> sign_in/
@user.route('/login', methods=['POST'])
def login():
    data = request.form.to_dict()

    data['remember_me'] = True if data['remember_me'] == 'true' else False
        

    try:
        validator = login_validator(data)
        user = validator.validate()
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202

    login_user(user, remember = data['remember_me'])
    return {"status":1, "message":"Login exitoso","user": user.serialize() }, 200
      

# Sign up -> sign_up
@user.route('/confirm_user', methods=['POST'])
def confirm_user():

    data = request.form.to_dict()

    try:
        validator = signup_validator(data)
        validator.validate()
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202

    data["role_id"] = "user"
    response = Users.add(data)

    if response > 0:
        # User registered succesfully
        return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
    else:
        return {"status":0, "message":"Hubo un error interno" }, 400




# get -> user/<username>
# delete -> delete/
# update -> update
# Password Recovery -> update




# Store API's Endpoints 
# Register Store
# Register company
# Register