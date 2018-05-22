from flask import Flask, request
from flask_restful import Resource, Api
from Services.Multiple import Multiple

app = Flask(__name__)
api = Api(app)

class api_rmultiple(Resource):
    def get(self, x1, x2, y):
        return Multiple().get_result(
            x1.split(','),
            x2.split(','),
            y.split(',')
        )
        

api.add_resource(
    api_rmultiple, 
    '/rlm/<x1>/<x2>/<y>'
)


if __name__ == '__main__':
    app.run(port=2409)
    