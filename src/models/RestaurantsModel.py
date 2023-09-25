from database.db import get_connection
from .entities.Restaurant import Restaurant
import uuid
class RestaurantModel():
    @classmethod
    def new_restaurant(cls, name, rating):
        try:
            connection = get_connection()  # Obtén una conexión a la base de datos

            with connection.cursor() as cursor:
                # Inserta un nuevo restaurante en la base de datos
               

                new_uuid = str(uuid.uuid4())  # Genera un nuevo UUID

                cursor.execute(
                    """
                    INSERT INTO public."Restaurants" (id, name, rating)
                    VALUES (%s, %s, %s)
                    RETURNING id;
                    """,
                    (new_uuid, name, rating)
                )
                
                new_restaurant_id = cursor.fetchone()[0]  # Obtiene el ID del nuevo restaurante

            connection.commit()  # Confirma la transacción
            connection.close()  # Cierra la conexión
            # Devuelve el ID del nuevo restaurante creado
            return new_restaurant_id
        except Exception as ex:
            print(ex)
            raise Exception(ex)
    @classmethod
    def update_restaurant(cls, id, name, rating):
        try:
            connection = get_connection()  # Obtén una conexión a la base de datos

            with connection.cursor() as cursor:
                # Actualiza el restaurante en la base de datos
                cursor.execute(
                    """
                    UPDATE public."Restaurants"
                    SET name = %s, rating = %s
                    WHERE id = %s
                    RETURNING id, name, rating;
                    """,
                    (name, rating, id)
                )

                updated_restaurant = cursor.fetchone()

            connection.commit()  # Confirma la transacción
            connection.close()  # Cierra la conexión

            if updated_restaurant:
                return Restaurant(*updated_restaurant)  # Devuelve el restaurante actualizado
            else:
                return None  # El restaurante no fue encontrado
        except Exception as ex:
            print(ex)
            raise Exception(ex)   
    @classmethod
    def delete_restaurant(cls, id):
        try:
            connection = get_connection()  # Obtén una conexión a la base de datos

            with connection.cursor() as cursor:
                # Elimina el restaurante de la base de datos
                cursor.execute(
                    """
                    DELETE FROM public."Restaurants"
                    WHERE id = %s
                    RETURNING id, name, rating;
                    """,
                    (id,)
                )

                deleted_restaurant = cursor.fetchone()

            connection.commit()  # Confirma la transacción
            connection.close()  # Cierra la conexión

            if deleted_restaurant:
                return Restaurant(*deleted_restaurant)  # Devuelve el restaurante eliminado
            else:
                return None  # El restaurante no fue encontrado
        except Exception as ex:
            print(ex)
            raise Exception(ex)  

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
                    SELECT id, name, rating, lat, ing
                    FROM public."Restaurants"
                    WHERE ST_DWithin(
                        ST_MakePoint(ing, lat)::geography,
                        ST_MakePoint(%s, %s)::geography,
                        %s
                    );
                    """,
                    (lng, lat, radius)
                )
                resultset=cursor.fetchall()
                for row in resultset:
                    restaurant = Restaurant(
                        id=row[0],
                        name=row[1],
                        rating=row[2],
                        lat=row[3],
                        ing=row[4]
                    )
                    restaurants.append(restaurant.to_JSON())

            connection.close()  # Cierra la conexión cuando hayas terminado de usarla
        except Exception as ex:
            print(ex)
            raise Exception(ex)

        return restaurants
