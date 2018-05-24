from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Resource, Api
from Services.Multiple import Multiple
from Services.Polynomial import Polynomial

app = Flask(__name__)
api = Api(app)

@app.route('/rlm/<x1>/<x2>/<y>')
def APIRmultiple(parameter_list):
    return Multiple().get_result(
            map( float, x1.split(',') ),
            map( float, x2.split(',') ),
            map( float, y.split(',') )
        )

@app.route('/rp/<x>/<y>')
def APIRpolynomial(x, y):
    return Polynomial().get_result(
            map(float, x.split(',')),
            map(float, y.split(','))
        )

@app.route('/')
def root():
    return render_template('information.html')


if __name__ == '__main__':
    app.run(port=2409)
    