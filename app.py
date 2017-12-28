import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') #lives at root folder - doesn't have to be sqlite
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sam'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth new end point

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': #means it only runs if we execute this file - not simply import
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
