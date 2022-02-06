from flask_restful import Resource
import requests
import os
import json
from flask import request
from helper import send_options, send_response

class Orders(Resource):
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            payload = request.get_json()
            response = save_order_details({"records":[{"fields":payload}]})
            if response.reason == 'OK':
                return send_response({}, 200)
            else:
                return send_response(response.text, 400)
        else:
            return send_response({"error": "invalid content type"}, 400)

    def options(self):
        return send_options("POST")

def save_order_details(payload):
    url = os.environ['AIRTABLE_URL']+'/orders'
    header = {"Authorization":"Bearer " + os.environ['AIRTABLE_KEY'], "Content-Type": "application/json"}
    
    return requests.post(url, data = json.dumps(payload), headers = header)

# sample airtable payload structure for dev reference
sample_payload = {
  "records": [
    {
      "fields": {
        "your-name": "claudia",
        "your-email": "claudia@sample.com",
        "phone-number": "9021111111",
        "pickup-location": "123 high st, Williamswood, Nova Scotia, Canada",
        "drop-location": "55 bently dr, Williamswood, Nova Scotia, Canada",
        "pickup-date": "2022-12-15",
        "item-description": "A wardrobe 73 inches high, 38 wide.\n2 regular sized doors, 3 closet doors, a few skinny windows, building materials 4 boxes of cedar shingles, 2 boxes...",
        "price": 115,
        "tos": 1,
        "record_date": "2022-12-16T02:46:00.000Z"
      }
    },
    {
      "fields": {
        "your-name": "prajwal",
        "your-email": "app@a.ca",
        "phone-number": "9029898888",
        "pickup-location": "8 Theakston Avenue, Halifax, Nova Scotia, Canada",
        "drop-location": "40 Theakston Avenue, Halifax, Nova Scotia, Canada",
        "pickup-date": "2021-12-10",
        "price": 85,
        "tos": 1,
        "record_date": "2021-12-12T03:21:00.000Z"
      }
    }
  ]
}
    