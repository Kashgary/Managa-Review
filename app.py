import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Manga, Review
from auth import AuthError, requires_auth

ITEMS_PER_PAGE = 10

def pagination(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    items = [item.format() for item in selection]
    pagination = items[start:end]

    return pagination

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  @app.after_request
  def after_request(response):
      response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type,Authorization,true')
      response.headers.add(
          'Access-Control-Allow-Methods',
          'GET,PUT,POST,DELETE,OPTIONS')
      return response
    
  @app.route('/manga_list', methods=['GET'])
  def get_mangas():
      selection = Manga.query.order_by(Manga.title).all()
      paginated_mangas = pagination(request, selection)
      
      if len(paginated_mangas) == 0:
          abort(404)
      return jsonify({
          'success': True,
          'mangas': paginated_mangas,
          'total_mangas': len(selection),
      })
  
  @app.route('/add_manga', methods=['POST'])
  @requires_auth('add:manga')
  def add_manga(jwt):
    body = request.get_json()

    if not (
            'title' in body and 'author' in body and
            'genre' in body and 'rating' in body
            ):
        abort(422)

    try:
        manga = Manga(
            title=body.get('title'),
            author=body.get('author'),
            genre=body.get('genre'),
            rating=body.get('rating')
            )
        manga.insert()

        return jsonify({
            'success': True,
            'created': manga.title,
        })

    except BaseException:
        abort(422)

  @app.route('/manga/<int:manga_id>/reviews', methods=['GET'])
  def get_reviews(manga_id):
      selection = Review.query.filter(
          Review.manga_id==manga_id).order_by(Review.id).all()
      paginated_reviews = pagination(request, selection)
      manga = Manga.query.with_entities(Manga.title).filter(Manga.id==manga_id).all()
      if len(paginated_reviews) == 0:
          abort(404)
      
      if not manga:
          abort(404)
      data =[]
      for review in paginated_reviews:
        data.append({
            "id": review.get('id'),
            "manga_id": review.get('manga_id'),
            "title": review.get('title'),
            "name": review.get('name')
        })
      return jsonify({
          'success': True,
          'manga': manga,
          'reviews': data,
          'total_reviews': len(selection),
      })

  @app.route('/review/<int:id>', methods=['GET'])
  def get_a_review(id):
      review = Review.query.filter(Review.id==id).all()
      if len(review) == 0:
          abort(404)
      items = [item.format() for item in review]
      return jsonify({
          'success': True,
          'review': items,
      })

  @app.route('/manga/<int:manga_id>/add_review', methods=['POST'])
  @requires_auth('add:review')
  def add_review(jwt,manga_id):
    body = request.get_json()
    manga = Manga.query.get(manga_id)
    print(body.get('title'))
    print(manga)
    if not (
            'name' in body and 'review' in body and
            'title' in body and 'rating' in body
            ):
        abort(422)
    if not manga:
        abort(404)
    try:
        review = Review(
            title=body.get('title'),
            name=body.get('name'),
            review=body.get('review'),
            rating=body.get('rating'),
            manga_id = manga_id
            )
        review.insert()

        return jsonify({
            'success': True,
            'created': review.title,
        })

    except BaseException:
        abort(422)

  @app.route("/review/<int:id>", methods=['DELETE'])
  @requires_auth('delete:review')
  def delete_review(id, jwt):
    manga_id = Review.query.with_entities(Review.manga_id).filter(Review.id==id).all()
    if not manga_id:
        abort(404)
        
    review = Review.query.get((id,manga_id[0]))
    
    if not review:
        abort(404)
    try:
        review.delete()
        return jsonify({
            'success': True,
            'deleted': id
        })
    except BaseException:
        abort(422)
  @app.route("/review/<id>", methods=['PATCH'])
  @requires_auth('edit:review')
  def update_drink(jwt, id):

    manga_id = Review.query.with_entities(Review.manga_id).filter(Review.id==id).all()
    if not manga_id:
        abort(404)
        
    review = Review.query.get((id,manga_id[0]))
    if not review:
        abort(404)

    try:
        body = request.get_json()
        
        title=body.get('title')
        name=body.get('name')
        review_body=body.get('review')
        rating=body.get('rating')
        
        if title:
            review.title = title
        if name:
            review.name = name
        if review:
            review.review = review_body
        if rating:
            review.rating = rating
            
        review.update()
        
        return jsonify({
            'success': True,
            'id': review.id,
            'title': review.title,
            'name':review.name,
            'review': review.review,
            'rating': review.rating,
            'manga_id': review.manga_id
        })
    except BaseException:
        abort(422)

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)