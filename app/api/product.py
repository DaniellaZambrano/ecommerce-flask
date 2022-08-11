from flask import Blueprint, jsonify, request
from flask_login import login_required, login_user
from .validators.add_product_validator import add_product_validator
import json
from ..logic.DAO.Products import Products as Items

item = Blueprint('item', __name__, url_prefix='/item/')

@item.route('/add', methods=['POST'])
def add():

    data = request.form.to_dict()

    try:
        validator = add_product_validator(data)
        validator.validate()
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202

    response = Items.add(data)

    if response > 0:
        # Product added succesfully
        return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
    else:
        return {"status":0, "message":"Hubo un error interno" }, 400
