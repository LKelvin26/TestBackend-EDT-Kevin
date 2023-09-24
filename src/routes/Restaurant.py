from flask import Blueprint,jsonify
from models.RestaurantsModel import RestaurantModel

main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_restaurants():
    try:

        restaurants=RestaurantModel.get_restaurants()
        return jsonify(restaurants)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
        
@main.route('/<id>')
def get_restaurant(id):
    try:
        restaurant=RestaurantModel.get_restaurant(id)
        if restaurant != None:
            return jsonify(restaurant)
        else: jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

    