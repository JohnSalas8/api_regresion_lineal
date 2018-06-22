from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_restful import Resource, Api
from Services.Multiple import Multiple
from Services.Polynomial import Polynomial

app = Flask(__name__)
api = Api(app)

# http://localhost:2409/rlm/0,2,2.5,1,4,7/0,1,2,3,6,2/5,10,9,0,3,27
@app.route('/rlm/<x1>/<x2>/<y>')
def APIRmultiple(x1, x2, y):
    return jsonify(
        Multiple().get_result(
            map( float, x1.split(',') ),
            map( float, x2.split(',') ),
            map( float, y.split(',') )
        )
    )

# http://localhost:2409/rlp/0,1,2,3,4,5/2.1,7.7,13.6,27.2,40.9,61.1
@app.route('/rlp/<x>/<y>')
def APIRpolynomial(x, y):
    return jsonify(
        Polynomial().get_result(
            map(float, x.split(',')),
            map(float, y.split(','))
        )
    )

# http://localhost/rls/
@app.route('/rls/<x>/<y>')
def APIRsimple(x, y):
    pass

@app.route('/')
def index():
    return render_template('information.html')


if __name__ == '__main__':
    app.run(port=2409)
    