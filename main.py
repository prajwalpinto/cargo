from flask import Flask
from flask_restful import Api
from pricer import Pricer
from quotes import Quotes
from helper import send_options, send_response


app = Flask(__name__)
api = Api(app)

api.add_resource(Quotes, '/quotes')
api.add_resource(Pricer, '/pricer')

if __name__ == '__main__':
    # app.run(debug=True) # run true for development 
    app.run() # production mode
