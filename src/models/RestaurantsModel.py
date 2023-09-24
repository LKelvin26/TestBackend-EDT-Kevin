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
                    restaurant=Restaurant(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    restaurants.append(restaurant.to_JSON())
            connection.close
            return restaurants
        except Exception as ex:
            print(ex)
            raise Exception(ex)
    
    def get_restaurant(self,id):
        try:
            connection=get_connection()
            restaurant=[]

            with connection.cursor () as cursor:
                cursor.execute("SELECT * FROM Restaurants WHERE id =%s",(id,))
                row=cursor.fetchone()

                movie=None
                if row != None:
                    restaurant=Restaurant(row[0],row[1],row[2],row[3])
                    restaurant=restaurant.to_JSON()

            connection.close
            return restaurant
        except Exception as ex:
            print(ex)
            raise Exception(ex)