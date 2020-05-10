import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Manga, Review


class MangaReviewTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "managa_review"
        self.database_path = "postgres://{}/{}".format('postgres:123@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_manga = {'title': "test", 'author': "test", 'genre': ['test'], 'rating': 1}
        self.new_review = 	{'name': "Kashgay3",
                            'rating': 10,
                            'review': "The story is about a boy named Bam and Bam the 25th, and Bam in Korean mean night. thus his name is the 25th night cuz he was born at that night",
	                        'title': "What Bam mean"
                            }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        pass


    def test_get_manga_lists(self):
        res = self.client().get('/manga_list')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_paginated_questions(self):
        res = self.client().get('/manga/2/reviews')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    

    def test_delete_review(self):
        res = self.client().delete('/review/5')
        data = json.loads(res.data)

        review = Review.query.filter(Review.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(review, None)
    
    def test_add_manga(self):
        res = self.client().post('/add_manga', json=self.new_manga)
        data = json.loads(res.data)
        pass

    def test_422_if_add_manga_fails(self):
        res = self.client().post('/add_manga', json=self.new_manga)
        data = json.loads(res.data)
        pass   

    def test_edit_review(self):
        res = self.client().patch('/review/5', json=self.new_review)
        data = json.loads(res.data)
        pass   
    
    def test_422_edit_review(self):
        res = self.client().patch('/review/5', json=self.new_review)
        data = json.loads(res.data)
        pass  
    
    def test_add_review(self):
        res = self.client().post('/manga/1/add_review', json=self.new_review)
        data = json.loads(res.data)
        pass
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
