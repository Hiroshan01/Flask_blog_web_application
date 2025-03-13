# class Config:
#     SECRET_KEY = 'hiroshan199#4$'
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:hiroshan@localhost/blogapp'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Hiro9999DS')  
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')  
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'
