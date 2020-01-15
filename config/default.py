import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG = True
SECRET_KEY = os.urandom(32)
