import os
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from api_models import CharacterResponse
from sqlalchemy import Column, Integer, String, Boolean
from api_config import DATABASE_NAME, DATABASE_PATH
from sqlalchemy.ext.serializer import dumps

app = Flask(__name__)
app.config.from_object('api_config.DevelopmentConfig')
database = SQLAlchemy(app)

class Character(database.Model):
    __tablename__ = 'characters_table'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    category = Column(String)
    dead = Column(Boolean)
    active = Column(Boolean)

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.dead = False
        self.active = False

    def __ref__(self):
        return '<Character(name: %s, class: %s, dead: %r, active: %r)>' % (self.name, self.category, self.dead, self.active)

    def toCharacterResponse(self):
        return CharacterResponse(
            id = self.id, 
            name = self.name,
            category = self.category,
            dead = self.dead,
            active = self.active
        )
        
if __name__ != '__main__':
    try:
        os.makedirs(DATABASE_PATH)
    except FileExistsError:
        # already exists so we'll continue
        pass
    
    if not os.path.exists('%s/%s' % (DATABASE_PATH, DATABASE_NAME)):
        database.create_all()
