import os
from dotenv import load_dotenv

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
load_dotenv()

database_name = 'trivia'
#  IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'Postgresql://postgres:TIMMY@localhost:5432/trivia'
SQLALCHEMY_TRACK_MODIFICATIONS= True