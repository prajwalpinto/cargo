from flask import Response
import json

def send_response(body, status):
    response = Response(json.dumps(body), status)
    response.headers['Content-Type']="application/json"
    response.headers.add("Access-Control-Allow-Origin", "*") # externally accessible. Change to domain name before release
    return response

def send_options(options):
    response = Response(status=200)
    response.headers.add("Access-Control-Allow-Origin", "*") # externally accessible. Change to domain name before release
    response.headers.add("Access-Control-Allow-Methods", options)
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response