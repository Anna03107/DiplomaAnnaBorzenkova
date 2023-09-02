import data
import configuration
import requests

def post_new_order():
    return requests.post(configuration.URL + configuration.CREATE_ORDER,
           json=data.order_body)

def get_order(track_number):
    return requests.get(configuration.URL + configuration.GET_ORDER,
           params={"t": track_number})