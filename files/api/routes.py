from flask import Flask, json, jsonify, request, make_response
from files.api.services import account_services, attribute_services, character_services, world_services
from files.database.db_utils import DUPLICATE_ENTRY
from json import JSONEncoder
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

@app.route('/', methods = ['GET'])
def index():
    return {'message': 'this is the index page'}, 200

@app.route('/accounts/sign_up', methods = ['POST'])
def sign_up():
    response = None
        
    id = account_services.sign_up(request.json)
    if id > 0:
        response = {'account_id': '%d'%id}, 200
    elif id == DUPLICATE_ENTRY:
        response = {'error': 'DUPLICATE_ENTRY'}, 400
        
    return response

@app.route('/accounts/sign_in', methods = ['POST'])
def sign_in():
    response = None
    
    account = account_services.sign_in(request.json)
    if account != None:
        response = account, 200
    else:
        response = {'error': 'NOT_FOUND'}, 400
    
    return response

@app.route('/accounts/<account_id>/delete', methods = ['DELETE'])
def delete_account(account_id: int):
    response = None
    
    rows_affected = account_services.delete_account(account_id)
    if rows_affected > 0:
        response = jsonify(success = True)
    else:
        response = {'error': 'NOT_FOUND'}, 400
    
    return response

@app.route('/<account_id>/worlds/<world_name>/create', methods = ['PUT'])
def create_world(account_id: int, world_name: str):
    world_id = world_services.create_world(account_id, world_name)    
    return {'world_id': world_id}, 200
    
@app.route('/<account_id>/worlds', methods = ['GET'])
def get_account_worlds(account_id: int):
    worlds = world_services.get_account_worlds(account_id)
    return jsonify(worlds), 200

@app.route('/worlds/<world_id>/delete', methods = ['DELETE'])
def delete_world(world_id: int):
    response = None
    
    rows_affected = world_services.delete_world(world_id)
    if rows_affected > 0:
        response = jsonify(success = True)
    else:
        response = {'error': 'NOT_FOUND'}, 400
    
    return response

@app.route('/worlds/<world_id>/attributes/create', methods = ['POST'])
def create_attribute(world_id: int):
    response = None
    attribute_id = attribute_services.create_attribute(world_id, request.json)
    
    if attribute_id > 0:
        response = {'world_id': world_id, 'attribute_id': attribute_id}, 200
    elif id == DUPLICATE_ENTRY:
        response = {'error': 'DUPLICATE_ENTRY'}, 400
        
    return response

@app.route('/worlds/<world_id>/attributes', methods = ['GET'])
def get_attributes_for_world(world_id: int):
    attributes = attribute_services.get_attributes_for_world(world_id)
    return jsonify(attributes), 200

@app.route('/<account_id>/worlds/<world_id>/characters/<char_name>/create', methods = ['PUT'])
def create_character(account_id: int, world_id: int, char_name: str):
    response = None
    char_id = character_services.create_character(account_id, world_id, char_name)
    
    if char_id > 0:
        response = {'character_id': char_id}, 200
    elif char_id == DUPLICATE_ENTRY:
        response = {'error': 'DUPLICATE_ENTRY'}, 400
        
    return response

@app.route('/<account_id>/worlds/<world_id>/characters', methods = ['GET'])
def get_account_characters(account_id: int, world_id: int):
    characters = character_services.get_characters_for_account(account_id, world_id)
    return jsonify(characters), 200

@app.route('/characters/<character_id>', methods = ['GET'])
def get_character_details(character_id: int):
    character = character_services.get_character_details(character_id)
    return character, 200