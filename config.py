from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
FLASK_ENV = os.getenv("FLASK_ENV")
SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@{2}/{3}".format(os.getenv("DB_USER"), os.getenv("DB_PSSWD"), os.getenv("DB_HOST"), os.getenv("DB_NAME"))
SQLALCHEMY_TRACK_MODIFICATIONS = False