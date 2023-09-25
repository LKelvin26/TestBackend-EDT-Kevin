Restaurant API Documentation
Introduction
The Restaurant API allows you to manage restaurant data, including creating, reading, updating, and deleting restaurant records. Additionally, you can calculate statistics for restaurants within a specified radius from a given latitude and longitude.

Endpoints
Create a New Restaurant
Endpoint: /create
Method: POST
Description: Create a new restaurant.
Request Body:
name (string): The name of the restaurant.
rating (float): The rating of the restaurant.
Response:
JSON response with the newly created restaurant.
Read a Restaurant by ID
Endpoint: /read/<id>
Method: GET
Description: Retrieve information about a restaurant by providing its unique ID.
Parameters:
id (string): The ID of the restaurant to retrieve.
Response:
JSON response with the restaurant's information.
Update a Restaurant by ID
Endpoint: /update/<id>
Method: PUT
Description: Update information about a restaurant by providing its unique ID and new data in the request body.
Parameters:
id (string): The ID of the restaurant to update.
Request Body:
name (string): The updated name of the restaurant.
rating (float): The updated rating of the restaurant.
Response:
JSON response with the updated restaurant.
Delete a Restaurant by ID
Endpoint: /delete/<id>
Method: DELETE
Description: Delete a restaurant by providing its unique ID.
Parameters:
id (string): The ID of the restaurant to delete.
Response:
JSON response indicating the success of the operation.
Calculate Statistics for Restaurants
Endpoint: /restaurants/statistics
Method: GET
Description: Calculate statistics (count, average rating, standard deviation of rating) for restaurants located within a specified radius from a given latitude and longitude.
Query Parameters:
latitude (float): Latitude coordinate.
longitude (float): Longitude coordinate.
radius (float): Radius in meters.
Response:
JSON response with the calculated statistics.


# Configuración de Variables de Entorno

# SECRET_KEY: Clave secreta utilizada para firmar cookies y proteger sesiones.
SECRET_KEY=1234

# PGSQL_HOST: Host del servidor de PostgreSQL.
PGSQL_HOST=localhost

# PGSQL_USER: Nombre de usuario de PostgreSQL.
PGSQL_USER=postgres

# PGSQL_PASSWORD: Contraseña de PostgreSQL.
PGSQL_PASSWORD=1234

# PGSQL_DATABASE: Nombre de la base de datos de PostgreSQL.
PGSQL_DATABASE=MelpDB

# FLASK_ENV: Entorno de Flask (development, production, etc.).
FLASK_ENV=development

Error Responses
400 Bad Request: Invalid input data.
404 Not Found: Restaurant not found.
500 Internal Server Error: Server error occurred.