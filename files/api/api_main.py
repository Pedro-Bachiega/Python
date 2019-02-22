import os
import api_database
import logging
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.serializer import loads, dumps

# this executes the file, also creating the database
api_database

database = api_database.database
app = api_database.app

@app.route('/', methods = ['GET'])
def index():
    return make_response(jsonify({'message': 'index'}))

if __name__ == '__main__':
    # this runs the api
    app.run(debug = True)