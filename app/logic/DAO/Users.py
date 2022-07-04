from .DAO import DAO
from ..models.User import User
from app import db
import bcrypt

class Users(DAO):
    """
    User Data Access Object Class.
    """

    def __init__(self):
        pass

    def add(data):
        """ 
        Adds to the Database
        """
        try:
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            print("Creating User....")
            user = User(data["identification_type"], data["identification_number"], data["cellphone"], data['role_id'], data["name"], data["last_name"], data["username"],data["birth_date"], data["email"], hashed_password.decode('utf8'), data["address"], data["alt_address"])
            print("user created")
            db.session.add(user)
            db.session.add(user.email)
            db.session.add(user.user_type)
            db.session.commit()

            return user.id
        except Exception as ex:
            print(ex.__repr__())
            return 0

    def get(self):
        """
        Gets alll records from the Database
        """
        users = User.query.all()

        return users

    def find(identification_number, identification_type):
        """
        Find a single record from the Database by id
        """
        user = User.query.filter_by(identification_number = identification_number).first()
        if user != None and user.identification_type is identification_type:
            return user
        
        return False

    def update(self, data):
        """
        Updates a Record on the Database 
        """
        try:
            user = User.query.filter_by(id = data['id']).first()

            user.name = data['name']
            user.lastname = data['last_name']
            user.email = data['email']
            user.cellphone = data['cellphone']
            user.username = data['username']
            user.businessName = data["businessName"]
            user.identification_type = data['identification_type']
            user.identification_number = data['identification_number']

            if data['password'] != '':
                hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
                user.password = hashed_password.decode('utf-8')
                
            db.session.commit()

            return user.id
        except Exception as ex:
            # traceback.print_exc()
            raise ex

    def update_status_store(self, data):
        """
        Updates a Record on the Database 
        """
        try:
            user = User.query.filter_by(id = data['id']).first()

            user.status = data['status']
               
            db.session.commit()

            return user.id
        except Exception as ex:
            # traceback.print_exc()
            raise ex
    def delete(self, id):
        """

        Deletes a record on the Database
        """
        pass


    def find_by_username(self, username):
        """
        Find an Operator by username
        """ 
        user = User.query.filter_by(username=username).first()


        return user

    def get_admins(self):
        """
        Find an Operator by username
        """ 
        users = User.query.filter_by(role_id=1).all()


        return users

    def get_companys(self):
        """
        Find an Operator by username
        """ 
        users = User.query.filter_by(role_id=4).all()


        return users

    def get_drivers(self):
        """
        Find an Operator by username
        """ 
        users = User.query.filter_by(role_id=5).all()


        return users

    def get_stores(self):
        """
        Find an Operator by username
        """
        users = User.query.filter_by(role_id=3).all()


        return users
