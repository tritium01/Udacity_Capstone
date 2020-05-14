import os
import json
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

database_name="agency"
database_path = "postgres://{}@{}/{}".format('postgres:RMGtri2018#','localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    
'''
Movies
'''
class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = Column(db.Integer, primary_key=True)
    title = Column(db.String)
    release = Column(db.String)
    
    def __init__(self, title, release):
        self.title = title
        self.release = release

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release
        }
'''
Actors
'''
class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(db.Integer(), primary_key=True)
    name = Column(db.String())
    age = Column(db.Integer())
    gender = Column(db.String())
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
