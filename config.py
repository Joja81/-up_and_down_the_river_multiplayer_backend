from os import environ, getcwd, path

port = 44535

url = f"http://localhost:{port}/"

#backend server url "https://up-and-down-the-river.herokuapp.com/"

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    # SECRET_KEY = environ.get('SECRET_KEY') DEAL WITH THIS LATER

    # Database
    
    directory = getcwd()
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{directory}/UpAndDownTheRiverMultiplayer.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False