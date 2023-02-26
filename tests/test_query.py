import json
import googlemaps
import os
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Dict
from pydantic import BaseModel


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

class Place(BaseModel):
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
