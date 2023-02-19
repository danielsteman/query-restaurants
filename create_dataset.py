import json
import googlemaps
import os
import time
from dotenv import load_dotenv


load_dotenv()

gmaps = googlemaps.Client(key=os.environ["API_KEY"])

jekerstraat = {
    "lat" : 52.3461957000798,
    "lng" : 4.899368098022659
}

params = {
    "location": jekerstraat,
    "radius": 1000,
    "open_now": True,
    "type": "restaurant",
}

def get_all_places(api_key: str = os.environ["API_KEY"]):
    gmaps = googlemaps.Client(key=api_key)
    query_results = []
    first_request = True
    while params.get("page_token") or first_request:
        first_request = False
        data = gmaps.places_nearby(**params)
        query_results.append(data)
        params["page_token"] = data.get("next_page_token")
        time.sleep(3)

    return query_results

with open("data/dataset.json", "w") as file:
    res = get_all_places()
    json.dump(res, file)

