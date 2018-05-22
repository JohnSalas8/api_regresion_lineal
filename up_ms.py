from flask import Flask, request
from flask_restful import Resource, Api
from Services.Multiple import Multiple

app = Flask(__name__)
api = Api(app)

class api_rmultiple(Resource):
    def get(self):
        return 'Regresion Lineal Multiple'
        

api.add_resource(api_rmultiple, '/regresion_lineal_multiple')


if __name__ == '__main__':
    app.run(port=2409)
    