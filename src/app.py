"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import requests
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

     response_body = {
         "msg": "Hello, this is your GET /user response "
     }

     return jsonify(response_body), 200

@app.route('/people', methods=['GET']) #get all people
def get_all_people():
    if request.method == 'GET':
        people = People.query.all() 
        serialized_people = [person.serialize() for person in people]
        return jsonify(serialized_people), 200
    
    else:
         return jsonify({'message': 'Invalid request method'}), 404

@app.route('/people/<int:person_id>', methods=['PUT', 'GET'])
def get_single_person(person_id):
     if request.method == 'GET':
          user1 = People.query.get(person_id)
          return jsonify(user1.serialize()), 200
     
     return "Person not found!" , 404

@app.route('/planets', methods=['GET'])
def handle_all_planets():
    if request.method == 'GET':
        planets = Planets.query.all()
        serialized_planet = [planets.serialize() for planets in planets]
        return jsonify(serialized_planet), 200
    
    else:
         return jsonify({'message': 'Invalid request method'}), 404
    
@app.route('/planets/<int:planet_id>', methods=['PUT', 'GET'])
def get_single_planet(planet_id):
     if request.method == 'GET':
          planet1 = Planets.query.get(planet_id)
          return jsonify(planet1.serialize()), 200
     
     return jsonify({'message': 'Planet not found!'}), 404
        
@app.route('/vehicles', methods =['GET'])
def handle_all_vehicles():
    if request.method == 'GET':
        vehicles = Vehicles.query.all()
        serialized_vehicles = [vehicles.serialize() for vehicles in vehicles]
        return jsonify(serialized_vehicles)
    
    else:
        return jsonify({'message': 'Invalid request method'}), 404


@app.route('/vehicles/<int:vehicle_id>', methods=['PUT', 'GET'])
def get_single_vehicle(vehicle_id):
     if request.method == "GET":
          vehicle1 = Vehicles.query.get(vehicle_id)
          return jsonify(vehicle1.serialize()),200
     
     return jsonify({'message': 'Vehicle not found!'}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
