import os
import json
from flask_migrate import Migrate
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
    release = Column(db.DateTime())

    
    def __init__(title, release):
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
    id = Column(db.Integer, primary_key=True)
    name = Column(db.Integer)
    age = Column(db.String)
    gender = Column(db.String)
    
    def __init__(name, age, gender):
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

'''
Two sets of specifications have been created for this project. The first set is general and not domain specified. This is for students who want to practice and have their own topic they want to use as the content for the project. Students who may not have their own idea can use the Casting Agency specifications to have slightly more structure when you get started.

General Specifications
Models will include at least…
Two classes with primary keys at at least two attributes each
[Optional but encouraged] One-to-many or many-to-many relationships between classes
Endpoints will include at least…
Two GET requests
One POST request
One PATCH request
One DELETE request
Roles will include at least…
Two roles with different permissions
Permissions specified for all endpoints
Tests will include at least….
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role
Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:

Movies with attributes title and release date
Actors with attributes name, age and gender
Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
Roles:
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role
'''