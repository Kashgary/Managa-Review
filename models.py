import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "managa_review"
database_path = "postgres://{}/{}".format('postgres:123@localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    
class Managa(db.Model):  
  __tablename__ = 'manga'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  author = db.Column(db.String)
  genre = db.Column(db.ARRAY(db.String()))
  rating = db.Column(db.Float())
  review = db.relationship("Review")
  
  def __init__(self, title, author, genre, rating):
    self.title = title
    self.author = author
    self.genre = genre
    self.rating = rating

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
      'author': self.author,
      'genre': self.genre,
      'rating': self.rating
    }

class Review(db.Model):  
  __tablename__ = 'review'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  name = db.Column(db.String)
  manga_id = db.Column(db.Integer, db.ForeignKey('manga.id'), primary_key=True)
  rating = db.Column(db.Float)
  

  def __init__(self, title, author, genre, rating, manga_id):
    self.title = title
    self.author = author
    self.genre = genre
    self.rating = rating
    self.manga_id = manga_id

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
      'manga_id': self.manga_id,
      'title': self.title,
      'name': self.name,
      'rating': self.rating
    }

