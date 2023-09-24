from flask import Blueprint,jsonify
from models.RestaurantsModel import RestaurantModel

main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_restaurants():
    try:

        movies=RestaurantModel.get_restaurants()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
        
@main.route('/<id>')
def get_restaurant(id):
    try:
        movie=RestaurantModel.get_restaurant(id)
        if movie != None:
            return jsonify(movie)
        else: jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

    