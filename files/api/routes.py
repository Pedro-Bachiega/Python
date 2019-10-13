from flask import Flask, json, jsonify, request, make_response
from files.api.services import account_services, attribute_services, character_services, world_services
from files.database.db_utils import DUPLICATE_ENTRY
from json import JSONEncoder
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def not_found(error):
    return jsonify(
            {
                'error': 'Not found'
            }
        ), 404

@app.route('/', methods = ['GET'])
def index():
    return jsonify(
        {
            'message': 'this is the index page'
        }
    )

@app.route('/accounts/sign_up', methods = ['POST'])
def sign_up():
    response = None
    content = request.json
    
    id = account_services.sign_up(content['user'], content['password'], content ['name'])
    if id > 0:
        response = jsonify(
            {
                'account_id': '%d'%id
            }
        ), 200
    elif id == DUPLICATE_ENTRY:
        response = jsonify({'error': 'DUPLICATE_ENTRY'}), 400
        
    return response

@app.route('/accounts/sign_in', methods = ['POST'])
def sign_in():
    response = None
    content = request.json
    
    account = account_services.sign_in(content['user'], content['password'])
    if account != None:
        response = account, 200
    else:
        response = jsonify({'error': 'NOT_FOUND'}), 400
    
    return response

@app.route('/accounts/<account_id>/delete', methods = ['DELETE'])
def delete_account(account_id: int):
    response = None
    
    rows_affected = account_services.delete_account(account_id)
    if rows_affected > 0:
        response = jsonify(success=True)
    else:
        response = jsonify({'error': 'NOT_FOUND'}), 400
    
    return response

@app.route('/<account_id>/worlds/<world_name>/create', methods = ['PUT'])
def create_world(account_id: int, world_name: str):
    world_id = world_services.create_world(account_id, world_name)
    worlds = world_services.get_account_worlds(account_id)
    last_index = len(worlds) - 1
    newest_world = worlds[last_index]
    
    return make_response(
        jsonify(
            {
                'world_id': newest_world.world_id,
                'public_id': newest_world.public_id
            }
        )
    )
    
@app.route('/<account_id>/worlds', methods = ['GET'])
def get_account_worlds(account_id: int):
    worlds = world_services.get_account_worlds(account_id)
    return jsonify(worlds)

@app.route('/worlds/<world_id>/delete', methods = ['DELETE'])
def delete_world(world_id: int):
    response = None
    
    rows_affected = world_services.delete_world(world_id)
    if rows_affected > 0:
        response = jsonify(success=True)
    else:
        response = jsonify({'error': 'NOT_FOUND'}), 400
    
    return response

@app.route('/worlds/<world_id>/attributes/create', methods = ['POST'])
def create_attribute(world_id: int):
    response = None
    content = request.json
    attribute_id = attribute_services.create_attribute(world_id, content['name'], content['description'], content['type'], content['negative_enabled'] == 'true')
    
    if attribute_id > 0:
        response = jsonify(
                {
                    'world_id': world_id,
                    'attribute_id': attribute_id
                }
            ), 200
    elif id == DUPLICATE_ENTRY:
        response = jsonify({'error': 'DUPLICATE_ENTRY'}), 400
        
    return response

@app.route('/worlds/<world_id>/attributes', methods = ['GET'])
def get_attributes_for_world(world_id: int):
    attributes = attribute_services.get_attributes_for_world(world_id)
    return make_response(jsonify(attributes))

@app.route('/<account_id>/worlds/<world_id>/characters/<char_name>/create', methods = ['PUT'])
def create_character(account_id: int, world_id: int, char_name: str):
    response = None
    char_id = character_services.create_character(account_id, world_id, char_name)
    
    if char_id > 0:
        response = jsonify(
                {
                    'character_id': char_id
                }
            ), 200
    elif char_id == DUPLICATE_ENTRY:
        response = jsonify({'error': 'DUPLICATE_ENTRY'}), 400
        
    return response

@app.route('/<account_id>/worlds/<world_id>/characters', methods = ['GET'])
def get_account_characters(account_id: int, world_id: int):
    characters = character_services.get_characters_for_account(account_id, world_id)
    return jsonify(characters)
