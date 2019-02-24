import os
import api_database
from api_database import Character, database, app
import logging
from flask import Flask, json, jsonify, request, make_response
from json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.serializer import loads, dumps
from xml.dom import minidom

configXml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.xml'))
configXml = minidom.parse(configXml_path)

xmlItems = configXml.getElementsByTagName('item')

server_ip = ''
server_port = 0

for item in xmlItems:
    if item.attributes['name'].value == 'server_ip':
        server_ip = str(item.firstChild.data)
    elif item.attributes['name'].value == 'server_port':
        server_port = int(item.firstChild.data)

# this executes the file, also creating the database
api_database

if server_ip == '':
    raise ValueError('No url provided')
elif server_port == 0:
    raise ValueError('No port provided')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods = ['GET'])
def index():
    return make_response(jsonify({'message': 'this is the index page'}))

@app.route('/example/<string:message>', methods = ['GET'])
def example(message):
    return jsonify({'message': message})

@app.route('/characters/create', methods = ['POST'])
def addChar():
    if not request.json or 'name' not in request.json or 'category' not in request.json:
        return jsonify({'code': 0, 'message': 'Incorrect values, please verify the sent json'})

    char_name = request.json['name']
    char_category = request.json['category']

    if database.session.query(Character).filter(Character.name == char_name).first():
        return jsonify({'code': 0, 'message': 'Name already registered, please choose another name'})

    database.session.add(Character(char_name, char_category))
    database.session.commit()

    char_id = database.session.query(Character).filter(Character.name == char_name).first().id

    return jsonify({'code': 1, 'message': 'Character created', 'char_id': char_id})

@app.route('/characters/newest_character', methods = ['GET'])
def getNewestCharacter():
    character = database.session.query(Character).order_by(Character.id.desc()).first()

    return character.toCharacterResponse().__repr__()

if __name__ == '__main__':
    # this runs the api
    app.run(host = server_ip, port = server_port, debug = True)