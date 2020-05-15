# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7
In order for current dependecies to work please use python 3.7 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

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

END POINT DESCRIPTION
```


GETS '/movies'
-Retrives an array with all movies inside database
-Required Arguments: none
-Required RBAC permission: requires 'get:movies' permission
-Returns an object with http response 200 key of success set to true and key of movie with an array containing all movies in the database

GETS '/actors'
-Retrives an array with all actors inside database
-Required Arguments: none
-Required RBAC permission: requires 'get:actors' permission
-Returns an object with http response 200 key of success set to true and key of actor with an array containing all actors in the database

POST '/movies'
-Adds a new movie
-Required Arguments: json including a key of name and release date
-Required RBAC permission: requires 'post:movie' permission
-Returns an object with http response 200 key of success set to true and key of movie with an array containing the movie just added

POST '/actors'
-Adds a new actor
-Required Arguments: json including a key of name and release date
-Required RBAC permission: requires 'post:actor' permission
-Returns an object with http response 200 key of success set to true and key of actor with an array containing the actor just added

PATCH '/movies/<int:movie_id>'
-Patches a specific actor based on the actor_id provided as a parameter
-Required Arguments: actor_id as a param used to patch that actor
-Required RBAC permission: requires 'patch:movie' permission
-Returns an object with http response 200 key of success set to true and key of movie with an array of the patched actor

PATCH '/actor/<int:actor_id>'
-Patches a specific actor based on the actor_id provided as a parameter
-Required Arguments: actor_id as a param used to patch that actor
-Required RBAC permission: requires 'patch:actor' permission
-Returns an object with http response 200 key of success set to true and key of actor with an array of the patched actor

DELETE '/movies/<movies_id>'
-Deletes a movie based on a integer id provided as a parameter
-Required Arguments: movie_id as a param used to delete that question
-Required RBAC permission: requires 'delete:actor' permission
-Returns an object with a key of success and value of true and key of movie with value of movie_id

DELETE '/actors/<actors_id>'
-Deletes an actor based on a integer id provided as a parameter
-Required Arguments: actor_id as a param used to delete that question
-Required RBAC permission: requires 'delete:actor' permission
-Returns an object with a key of success and value of true and key of artist with value of artist_id
```


## Testing
To run the tests, run
```
dropdb agency_test
createdb agency_test
python test_app.py
```
