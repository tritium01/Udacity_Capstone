import os
import json
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS
from .agency_models.models import setup_db, Actor, Movie
from .auth.auth import requires_auth, AuthError

def create_app(test_config=None):
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

    # MOVIE ROUTES
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = Movie.query.all()
        formated_movies = [movie.format() for movie in movies]
        
        return jsonify({
            'success': True,
            'movies': formated_movies    
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie(jwt):
        data = request.get_json()
        try:
            movie = Movie(
                title = data.get('title'),
                release = data.get('release')
            )
            
            movie.insert()
            new_movie = (
                Movie.query
                .filter_by(title = data.get('title'))
                .one_or_none()
            )
            return({
                "success": True,
                "movie": [new_movie.format()]
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def modify_movie(jwt, movie_id):
        data = request.get_json()
        movie= (
            Movie.query
            .filter_by(id = movie_id)
            .one_or_none()
        )
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
    def delete_movie(jwt, movie_id):
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
    def get_actor(jwt):
        actors = Actor.query.all()
        formated_actors = [actor.format() for actor in actors]
        
        return jsonify({
            'success': True,
            'actors': formated_actors
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(jwt):
        data = request.get_json()
        try:
            actor = Actor(
                name = data.get('name'),
                age = data.get('age'),
                gender = data.get('gender') 
            )
            actor.insert()
            new_actor = (
                Actor.query
                .filter_by(name = data.get('name'))
                .one_or_none()
            )
            return jsonify({
                'success': True,
                'actor': [new_actor.format()]
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def modify_actor(jwt, actor_id):
        data = request.get_json()
        actor = (
            Actor.query
            .filter_by(id = actor_id)
            .one_or_none()
        )
        try:
            actor.name = data.get('name')
            actor.age = data.get('age')
            actor.gender = data.get('gender')

            actor.update()
            return({
                'success': True,
                'actor': [actor.format()]
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        try:
            actor = (
                Actor.query
                .filter_by(id = actor_id)
                .one_or_none()
            )
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

    return app

