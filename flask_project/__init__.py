from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:2201@localhost:5432/proj'
db=SQLAlchemy(app)
from flask_project import routes

