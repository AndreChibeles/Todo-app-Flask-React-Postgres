from flask import Flask
from flask_restful import Resource

class Item(Resource):
    def get(self):
        return {'message': 'Hello World'}