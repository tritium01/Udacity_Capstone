import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from src.main import create_app
from src.agency_models.models import setup_db, Actor, Movie
from src.auth.get_token import get_auth_token


executive_producer_jwt = get_auth_token('executive producer')
casting_director_jwt = get_auth_token('casting director')
casting_assistant_jwt = get_auth_token('casting assistant')

class AgencyTestCase(unittest.TestCase):
    def setUp(self):
            """Define test variables and initialize app."""
            self.app = create_app()
            self.client = self.app.test_client
            self.database_name = "agency_test"
            self.database_path = "postgresql://{}:{}@{}/{}".format('postgres','RMGtri2018#','localhost:5432', self.database_name)
            setup_db(self.app, self.database_path)

            # binds the app to the current context
            with self.app.app_context():
                self.db = SQLAlchemy()
                self.db.init_app(self.app)
                # create all tables
                self.db.create_all()
            
            #setup mock data
            movie1 = Movie(
            title = "test102",
            release = "2021-05-12 19:40:01.918917"
            )
            movie2 = Movie(
            title = "test102",
            release = "2021-05-12 19:40:01.918917"
            )
            movie3 = Movie(
            title = "test102",
            release = "2021-05-12 19:40:01.918917"
            )
            movie1.insert()
            movie2.insert()
            movie3.insert()
            
            artist1 = Actor(
                name = "Ban Jovi",
                age = 24,
                gender = "male"
            )
            artist2 = Actor(
                name = "Ban Jovi",
                age = 24,
                gender = "male"
            )
            artist3 = Actor(
                name = "Ban Jovi",
                age = 24,
                gender = "male"
            )
            artist1.insert()
            artist2.insert()
            artist3.insert()
            
    def tearDown(self):
        """Executed after reach test"""
        pass

# EXECUTIVE PRODUCER TESTING
    def test_get_movies_executive_producer(self):
        res = self.client().get('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors_executive_producer(self):
        res = self.client().get('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movies_executive_producer(self):
        res = self.client().post('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])}, json={"title": "test101","release": "2020-05-12 19:40:01.918917"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_post_actors_executive_producer(self):
        res = self.client().post('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])}, json={"name": "Bon Javi 1","age": 28, "gender": "male"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_patch_movies_executive_producer(self):
        res = self.client().patch('/movies/1', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])}, json={"title": "test102","release": "2021-05-12 19:40:01.918917"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
    
    def test_patch_actors_executive_producer(self):
        res = self.client().patch('/actors/1', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])}, json={"name": "Bon Javij 1", "age": 20, "gender": "female"})
        data = json.loads(res.data)
        print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_delete_movies_executive_producer(self):
        res = self.client().delete('/movies/1', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_delete_movies_executive_producer(self):
        res = self.client().delete('/actors/1', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(executive_producer_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
# CASTING DIRECTOR TESTING
    def test_get_movies_director(self):
        res = self.client().get('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_get_actors_director(self):
        res = self.client().get('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_post_movies_director(self):
        res = self.client().post('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])}, json={"title": "test101","release": "2020-05-12 19:40:01.918917"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_post_actors_director(self):
        res = self.client().post('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])}, json={"name": "Bon Javi 1","age": 28, "gender": "male"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
    
    def test_patch_movies_director(self):
        res = self.client().patch('/movies/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])}, json={"title": "test102","release": "2021-05-12 19:40:01.918917"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
    
    def test_patch_actors_director(self):
        res = self.client().patch('/actors/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])}, json={"name": "Bon Javij 1", "age": 20, "gender": "female"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_delete_movies_casting_director(self):
        res = self.client().delete('/movies/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movies_casting_director(self):
        res = self.client().delete('/actors/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_director_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
# CASTING ASSISTANT TESTING
    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_get_actors_assistant(self):
        res = self.client().get('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_post_movies_assistant_401(self):
        res = self.client().post('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])}, json={"title": "test101","release": "2020-05-12 19:40:01.918917"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        

    def test_post_actors_assistant_401(self):
        res = self.client().post('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])}, json={"name": "Bon Javi 1","age": 28, "gender": "male"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movies_assistant(self):
        res = self.client().patch('/movies/3', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])}, json={"title": "test102","release": "2021-05-12 19:40:01.918917"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
    def test_patch_actors_assistant(self):
        res = self.client().patch('/actors/3', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])}, json={"name": "Bon Javij 1", "age": 20, "gender": "female"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movies_casting_assistant(self):
        res = self.client().delete('/movies/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movies_casting_assistant(self):
        res = self.client().delete('/actors/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %(casting_assistant_jwt["access_token"])})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

if __name__ == "__main__":
    unittest.main()