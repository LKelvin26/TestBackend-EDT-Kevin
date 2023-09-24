from database.db import get_connection
from .entities.Restaurant import Restaurant

class RestaurantModel():

    @classmethod 
    def get_restaurants(self):
        try:
            connection=get_connection()
            restaurants=[]

            with connection.cursor () as cursor:
                cursor.execute("SELECT * FROM public.\"Restaurants\" ORDER BY id ASC;")
                resultset=cursor.fetchall()

                for row in resultset:
                    restaurant=Restaurant(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    restaurants.append(restaurant.to_JSON())
            connection.close
            return restaurants
        except Exception as ex:
            print(ex)
            raise Exception(ex)
    
    def get_restaurant(id):
        try:
            connection=get_connection()
            restaurant=[]

            with connection.cursor () as cursor:
                cursor.execute("SELECT * FROM public.\"Restaurants\" WHERE id = %s", (id,))
                
                row=cursor.fetchone()

                
                if row != None:
                    restaurant=Restaurant(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    restaurant=restaurant.to_JSON()
                else:
                    return restaurant

            connection.close
            return restaurant
        except Exception as ex:
            print(ex)
            raise Exception(ex)
    
    def get_restaurant_in_radius(lat, lng, radius):
    # Establece la conexión a la base de datos
        try:
            connection = get_connection()  # Asegúrate de implementar la función get_connection() para obtener una conexión válida.

            restaurants = []

            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, lat, ing
                    FROM public."Restaurants"
                    WHERE ST_DWithin(
                        ST_MakePoint(ing, lat)::geography,
                        ST_MakePoint(%s, %s)::geography,
                        %s
                    );
                    """,
                    (lng, lat, radius)
                )
                row=cursor.fetchall()
                print(row)
                for rows in row:
                    restaurant = {
                        'id': rows[0],
                        'nombre': rows[1],
                        'lat': rows[2],
                        'lng': rows[3]
                    }
                    restaurants.append(restaurant)

            connection.close()  # Cierra la conexión cuando hayas terminado de usarla
        except Exception as ex:
            print(ex)
            raise Exception(ex)

        return restaurants
