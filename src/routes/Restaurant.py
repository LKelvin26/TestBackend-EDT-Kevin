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
    
@main.route('/restaurants/statistics?latitude=<x>&longitude=<y>&radius=<z>')

def calculate_statistics(x, y, z):
    try:
        restaurants=RestaurantModel.get_restaurant_in_radius(x,y,z)
         # Inicializa variables para calcular estadísticas
        count = len(restaurants)
        total_rating = 0.0

        # Calcula la suma de las calificaciones
        for restaurant in restaurants:
            total_rating += restaurant['rating']

        # Calcula el promedio de calificaciones
        if count > 0:
            avg_rating = total_rating / count
        else:
            avg_rating = 0.0

        # Calcula la desviación estándar de calificaciones
        std_rating = 0.0
        if count > 0:
            sum_squared_diff = sum((restaurant['rating'] - avg_rating) ** 2 for restaurant in restaurants)
            std_rating = (sum_squared_diff / count) ** 0.5

        # Devuelve los resultados en formato JSON
        results = {
            'count': count,
            'avg': avg_rating,
            'std': std_rating
        }

        return jsonify(results)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    