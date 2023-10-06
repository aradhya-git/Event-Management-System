import requests

def api_call(api_endpoint, request_dict):

  response = requests.post(api_endpoint, request_dict, apikey)

  return response
