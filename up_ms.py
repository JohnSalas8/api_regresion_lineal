from flask import Flask, request
from flask_restful import Resource, Api
from Services.Multiple import Multiple
from Services.Polynomial import Polynomial

app = Flask(__name__)
api = Api(app)

class api_rmultiple(Resource):
    def get(self, x1, x2, y):
        return Multiple().get_result(
            map( float, x1.split(',') ),
            map( float, x2.split(',') ),
            map( float, y.split(',') )
        )

class api_rpolynomial(Resource):
    def get(self, x, y):
        return Polynomial().get_result(
            map(float, x.split(',')),
            map(float, y.split(','))
        )
        

api.add_resource(
    api_rmultiple, 
    '/rlm/<x1>/<x2>/<y>'
)

api.add_resource(
    api_rpolynomial,
    '/rp/<x>/<y>'
)


if __name__ == '__main__':
    app.run(port=2409)
    