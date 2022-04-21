from flask import Flask
from flask_login import LoginManager
# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

config = app.config


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
    from .models import User
    return User.query.get(user_id)