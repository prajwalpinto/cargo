from flask import Flask, request, Response
from flask_restful import Resource, Api
from pricer import ( Pricer)


app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        return {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.']
        },
        'Linus': {
            'quote': ['Talk is cheap. Show me the code.']
            }
        }



api.add_resource(Quotes, '/quotes')
api.add_resource(Pricer, '/pricer')

if __name__ == '__main__':
    # app.run(debug=True) # run true for development 
    app.run() # production mode
