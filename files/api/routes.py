from flask import Flask, json, jsonify, request, make_response
from files.api.services import account_services, attribute_services, character_services, world_services
from files.models import Attribute
from files.database.db_utils import DUPLICATE_ENTRY
from json import JSONEncoder
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

duplicate_entry_response = make_response(jsonify({'error': 'DUPLICATE_ENTRY'}), 400)
not_found_response = make_response(jsonify({'error': 'NOT_FOUND'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify(
            {
                'error': 'Not found'
            }
        ),
        404
    )

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
        )
    elif id == DUPLICATE_ENTRY:
        response = duplicate_entry_response
        
    return response

@app.route('/accounts/sign_in', methods = ['POST'])
def sign_in():
    response = None
    content = request.json
    
    account = account_services.sign_in(content['user'], content['password'])
    if account != None:
        response = jsonify(account.__repr__())
    else:
        response = not_found_response
    
    return response

@app.route('/accounts/delete/<account_id>', methods = ['DELETE'])
def delete_account(account_id: int):
    response = None
    
    rows_affected = account_services.delete_account(account_id)
    if rows_affected > 0:
        response = jsonify(success=True)
    else:
        response = not_found_response
    
    return response

@app.route('/<account_id>/worlds/create/<name>', methods = ['PUT'])
def create_world(account_id: int, name: str):
    world_id = world_services.create_world(account_id, name)
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
    worlds_as_json = []
        
    if len(worlds) > 0:
        for i in range(0, len(worlds)):
            worlds_as_json.append(worlds[i].__repr__())
    
    return make_response(jsonify(worlds_as_json))

@app.route('/worlds/<world_id>/delete', methods = ['DELETE'])
def delete_world(world_id: int):
    response = None
    
    rows_affected = world_services.delete_world(world_id)
    if rows_affected > 0:
        response = jsonify(success=True)
    else:
        response = not_found_response
    
    return response

@app.route('/worlds/<world_id>/attributes/create', methods = ['POST'])
def create_attribute(world_id: int):
    response = None
    content = request.json
    attribute_id = attribute_services.create_attribute(world_id, content['name'], content['description'], content['type'], content['negative_enabled'] == 'true')
    
    if attribute_id > 0:
        response = make_response(
            jsonify(
                {
                    'world_id': world_id,
                    'attribute_id': attribute_id
                }
            )
        )
    elif id == DUPLICATE_ENTRY:
        response = duplicate_entry_response
        
    return response

@app.route('/worlds/<world_id>/attributes', methods = ['GET'])
def get_attributes_for_world(world_id: int):
    attributes = attribute_services.get_attributes_for_world(world_id)
    attributes_as_json = []
    
    if len(attributes) > 0:
        for i in range(0, len(attributes)):
            attributes_as_json.append(attributes[i].__repr__())

    return make_response(jsonify(attributes_as_json))

@app.route('/<account_id>/worlds/<world_id>/characters/create', methods = ['POST'])
def create_character(account_id: int, world_id: int):
    response = None
    content = request.json
    char_id = character_services.create_character(account_id, world_id, content['name'])
    
    if char_id > 0:
        response = make_response(
            jsonify(
                {
                    'character_id': char_id
                }
            )
        )
    elif char_id == DUPLICATE_ENTRY:
        response = duplicate_entry_response
        
    return response
