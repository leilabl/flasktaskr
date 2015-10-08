import os
import random
#import pdb; pdb.set_trace()

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(16)
#import pdb; pdb.set_trace()
# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
