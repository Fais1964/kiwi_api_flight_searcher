import os

import requests
import os
import json

ENDPOINT_SHEETY = os.getenv("ENDPOINT_SHEETY")

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=ENDPOINT_SHEETY)
        json_string = response.text

        data = json.loads(json_string)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{ENDPOINT_SHEETY}/{city['id']}",
                json=new_data
            )
            print(response.text)