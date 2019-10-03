import json
from datetime import datetime

with open('input.json') as json_file:
    data = json.load(json_file)
    for y in data["rentals"]:
        for x in data["cars"]:
            if x["id"]==y["car_id"]:
                d1 = datetime.strptime(y["start_date"], "%Y-%m-%d")
                d2 = datetime.strptime(y["end_date"], "%Y-%m-%d")
                number_of_days = abs((d2 - d1).days)+1
                time_component=0
                if number_of_days>10:
                    time_component=(number_of_days-10)*0.5*x["price_per_day"]+6*0.7*x["price_per_day"]+3*0.9*x["price_per_day"]+1*x["price_per_day"]
                elif number_of_days>4:
                    time_component=(number_of_days-4)*0.7*x["price_per_day"]+3*0.9*x["price_per_day"]+1*x["price_per_day"]
                elif number_of_days>1:
                    time_component=(number_of_days-1)*0.9*x["price_per_day"]+1*x["price_per_day"]
                else:
                    time_component=x["price_per_day"]

                distance_component = y["distance"]*x["price_per_km"]
                rental_price = time_component + distance_component

                commission = rental_price*0.3
                insurance = commission*0.5
                road_assistance = number_of_days*100
                drivy = commission - (insurance+road_assistance)
                print(insurance)
                print(road_assistance)
                print(drivy)
