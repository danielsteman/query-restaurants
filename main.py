import json
import googlemaps
import os
import time
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Dict


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

@dataclass
class Place:
    id: str
    name: str
    location: Dict[str, float]

mock_query_results = []

with open("mock.json") as f:
    data = json.load(f)
    next_page_token = data["next_page_token"]

    res = data["results"]

    for place in res:

        mock_query_results.append(Place(
            id=place["place_id"],
            name=place["name"],
            location=place["geometry"]["location"],
        ))


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

res = get_all_places()
print(res)
