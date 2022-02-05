from operator import add
import googlemaps
import os
from flask import request, Response
from flask_restful import Resource
gmaps = googlemaps.Client(key=os.environ['API_KEY'])

class Pricer(Resource):
    def post(self):
        content_type = request.headers.get('Content-Type')
        print('******', content_type)
        print('^^^^^^^')
        print(request.headers)
        if (content_type == 'application/json'):
            payload = request.get_json()
            print('--------')
            print(payload)
            print('--------')
            result = calculate_price(payload)
            if result: 
                response = Response(result, status=200)
                # response.headers.add("Access-Control-Allow-Origin", "*")
                return response
            else:
                response = Response("invalid request params", status=400)
                # response.headers.add("Access-Control-Allow-Origin", "*")
                return response
        else:
            response = Response("The response body goes here", status=400)
            # response.headers.add("Access-Control-Allow-Origin", "*")
            return response

    def options(self):
        response = Response(status=200)
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        response.headers.add("Access-Control-Allow-Headers", "*")
        return response



    
def get_distance(payload):
    distance =  gmaps.distance_matrix(origins=payload['origin'], destinations = payload['destination'], 
                                      mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
    return distance

def distance_price(distance):
    if (distance <=7000) :
      return 70
    elif(distance > 7000 and distance <=15000):
      return 80
    elif(distance >15000 and distance <=20000):
      return 90
    elif(distance >20000 and distance <=25000):
      return 100
    elif(distance >25000 and distance <=30000):
      return 110
    elif(distance >30000 and distance <=35000):
      return 120
    elif(distance >35000 and distance <=40000):
      return 150
    elif(distance >40000 and distance <=60000):
      return 200
    elif(distance >60000 and distance <=100000):
      return 250
    else:
      return 400

def additional_pricing(payload):
    price = 0
    items = payload['items-count']
    if(items == 'Two'): price+=10
    if(items == 'Three'): price+=20
    if(items == 'Four'): price+=30
    if(items == 'Five'): price+=40
    if(payload['curbside']): price+=5
    if(payload['stairs']): price+=20
    return price

def calculate_price(payload):
    return distance_price(get_distance(payload)) + additional_pricing(payload)