import os
import json
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS

from models import Movie, Actor, setup_db, db
from auth.auth import AuthError, requires_auth

# create and configure the app
app = Flask(__name__)
setup_db(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})    
#CORS Headers
@app.after_request    
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,POST,DELETE,OPTIONS')
    return response


'''
ROUTES
'''
# MOVIE ROUTES
@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies():
    movies = Movie.query.all()
    formated_movies = [movie.format() for movie in movies]
    
    return jsonify({
        'success': True,
        'movies': formated_movies    
    })

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def add_movie(jwt):
    data = request.get_json()
    try:
        new_movie = Movie(
            title = data.get('title'),
            release = data.get('release')
        )
        new_movie.insert()

        return jsonify({
            'success': True,
            'movie': new_movie
        })
    except:
        abort(422)

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movie')
def modify_movie(jwt, movie_id):
    data = request.get_json()
    movie= Movie.query.filter_by(id = movie_id).one_or_none()
    try:
        movie.title = data.get('title')
        movie.release = data.get('release')
        
        movie.update()

        return({
            'success': True,
            'movie': [movie.format()]
        })
    except:
        abort(422)
        
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def modify_movie(jwt, movie_id):
    try:
        movie = Movie.query.filter_by(id = movie_id).one_or_none()
        movie.delete()

        return({
            'success': True,
            'movie': movie_id
        })
    except:
        abort(422)

# Actor Routes

@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actor():
    actors = Actor.query.all()
    formated_actors = [actor.format() for actor in actors]
    
    return jsonify({
        'success': True,
        'actors': formated_actors
    })

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def add_actor(jwt):
    data = request.get_json()
    try:
        new_actor = Actor(
            name = data.get('name'),
            age = data.get('age'),
            gender = data.get('gender') 
        )
        new_actor.insert()
        
        return jsonify({
            'success': True,
            'actor': [new_actor.format()]
        })
    except:
        abort(422)

@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('PATCH:actor')
def modify_actor(jwt, actor_id):
    data = request.get_json()
    actor = Actor.query.filter_by(id = actor_id)
    try:
        actor.name = data.get('name')
        actor.age = data.get('age')
        actor.gender = data.get('gender')

        return({
            'success': True,
            'actor': [actor.format()]
        })
    except:
        abort(422)

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('DELETE:actor')
def modify_actor(jwt, actor_id):
    try:
        actor = Actor.query.filter_by(id = actor_id)
        actor.delete()
    
        return({
            'success': True,
            'actor': actor_id
        })
    except:
        abort(422)
    
#Error Handlers

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


'''
@DONE implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with appropriate messages):
    jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
        }), 404

'''
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
                    "success": False,
                    "error": 400,
                    "message": "Bad Request"
                    }), 400


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
                    "success": False,
                    "error": 403,
                    "message": "Forbidden"
                    }), 403


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Error"
    }), 500


@app.errorhandler(AuthError)
def auth_error(ex):
    return jsonify({
                    "success": False,
                    "error": ex.status_code,
                    "message": ex.error['code']
                    }),  ex.status_code


if __name__ == '__main__':
    app.run()