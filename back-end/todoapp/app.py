from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from resources.item import Item


app = Flask(__name__)
api = Api(app)

api.add_resource(Item, '/api/item')


if __name__ == '__main__':
    app.run(port=5000, debug=True)