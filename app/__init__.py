from flask import Flask
from flask_login import LoginManager
from flask import session
from config import *
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

config = app.config
app.secret_key = SECRET_KEY

# Flask Database
db = SQLAlchemy(app)
db.init_app(app)
from os import path
if not path.exists('../dev'):
    db.create_all()
    print('Created Database!')



# Flask Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return {"error":"Endpoint not found"}, 404

#If the user is not authorizewd to use the endpoint
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return {
        "status":0,
        "message":"User not authorized"
    }, 202

@login_manager.user_loader
def load_user(user_id):
    from .logic.DAO import Users
    return Users.find(user_id)


from app.api.user import user
app.register_blueprint(user)