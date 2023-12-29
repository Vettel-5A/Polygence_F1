import requests
import pandas as pd
import private.secret
import requests


class EuroSpecific:
    def __init__(self):
        self.europe_df = pd.read_csv('CodeSample/coordinates/europe_coordinates.csv')
        self.api_url = "http://www.mapquestapi.com/directions/v2/route"

    def get_driving_distance(self, start_location, end_location):
        params = {
            "key": private.secret.key,
            "from": start_location,
            "to": end_location,
        }

        try:
            response = requests.get(self.api_url, params=params)
            data = response.json()

            # Check if the request was successful
            if response.status_code == 200 and data["info"]["statuscode"] == 0:
                distance = data["route"]["distance"]


            
                print(f"Driving distance between {start_location} and {end_location}: {distance} miles")
                return distance
            else:
                print(f"Error: {data['info']['messages'][0]}")
        except Exception as e:
            print(f"Error: {e}")
