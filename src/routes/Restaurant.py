from flask import Blueprint,jsonify, request
from models.RestaurantsModel import RestaurantModel


main=Blueprint('restaurant_blueprint',__name__)
### CREATE
@main.route('/create',methods=['GET', 'POST'])
def create_restaurant():
    try:
        data = request.get_json()  # Obtén los datos JSON enviados en la solicitud

        # Extrae los campos del objeto JSON
        name = data.get('name')
        rating = int(data.get('rating'))
        
        # Valida y procesa los datos según sea necesario

        # Crea un nuevo restaurante en la base de datos
        new_restaurant = RestaurantModel.new_restaurant(name=name, rating=rating)
        

        # Devuelve una respuesta JSON con el nuevo restaurante
        return jsonify({'message': 'Restaurante creado exitosamente', 'restaurant': new_restaurant})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
### UPDATE
@main.route('/update/<id>', methods=['GET','POST'])
def update_restaurant(id):
    try:
        data = request.get_json()  # Obtiene los datos JSON enviados en la solicitud

        # Extrae los campos del objeto JSON (por ejemplo, name y rating)
        name = data.get('name')
        rating = int(data.get('rating'))

        # Llama a la función de modelo para actualizar el restaurante
        updated_restaurant = RestaurantModel.update_restaurant(id, name, rating)

        # Verifica si se encontró y actualizó el restaurante
        if updated_restaurant:
            return jsonify({'message': 'Restaurante actualizado exitosamente', 'restaurant': updated_restaurant.to_JSON()})
        else:
            return jsonify({'error': 'Restaurante no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
### DELETE
@main.route('/delete/<id>', methods=['GET','POST'])
def delete_restaurant(id):
    try:
        # Llama a la función de modelo para eliminar el restaurante
        deleted_restaurant = RestaurantModel.delete_restaurant(id)

        # Verifica si se encontró y eliminó el restaurante
        if deleted_restaurant:
            return jsonify({'message': 'Restaurante eliminado exitosamente', 'restaurant': deleted_restaurant.to_JSON()})
        else:
            return jsonify({'error': 'Restaurante no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
### READ
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
### 


### Task 2
@main.route('/statistics', methods=['GET'])
def calculate_statistics():
    try:
        # Obtén los parámetros de consulta desde request.args
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        radius = float(request.args.get('radius'))
        print(latitude)
        restaurants = RestaurantModel.get_restaurant_in_radius(latitude, longitude, radius)
        
         # Inicializa variables para calcular estadísticas
        count = len(restaurants)
        total_rating = 0.0

        # Calcula la suma de las calificaciones
        for restaurant in restaurants:
            total_rating += float(restaurant['rating'])

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
        return jsonify({'message': str(ex)}), 500
