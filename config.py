import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'attendance.db')
# change for production
SECRET_KEY = 'dev_key' 
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True