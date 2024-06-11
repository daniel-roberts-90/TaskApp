import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Saylor!'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:password@localhost:5432/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False