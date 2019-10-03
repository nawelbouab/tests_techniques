import json
from datetime import datetime
from collections import OrderedDict

with open('input.json') as json_file:
    data = json.load(json_file)
    #print(data)
    for y in data["rentals"]:
        for x in data["cars"]:
            if x["id"]==y["car_id"]:
                d1 = datetime.strptime(y["start_date"], "%Y-%m-%d")
                d2 = datetime.strptime(y["end_date"], "%Y-%m-%d")
                time_component = x["price_per_day"]*(abs((d2 - d1).days)+1)
                distance_component = y["distance"]*x["price_per_km"]
                rental_price = time_component + distance_component
                print(rental_price)
