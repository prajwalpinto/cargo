from flask_restful import Resource
from helper import send_options, send_response

class Quotes(Resource):
    # sample api for testing
    def get(self):
        response  = {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.']
        },
        'Linus': {
            'quote': ['Talk is cheap. Show me the code.']
            }
        }
        return send_response(response, 200)
    def options(self):
        return send_options("GET")
