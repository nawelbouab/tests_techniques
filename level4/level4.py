import json
from datetime import datetime


rentals_list = dict()
rentals_list["rentals"] = []

with open("input.json") as json_file:
    data = json.load(json_file)
    #print(data)
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
                rental_price = int(time_component + distance_component)


                commission = rental_price*0.3
                insurance = int(commission/2)
                assistance = number_of_days*100
                drivy = int(commission - insurance - assistance)


                rental = dict()
                rental["id"] = y["id"]
                rental["actions"] = []

                for i in ["driver", "owner", "insurance", "assistance", "drivy"]:
                    action = dict()
                    action["who"] = i
                    if i == "driver":
                        action["type"] = "debit"
                        action["amount"] = rental_price
                    else:
                        action["type"] = "credit"
                        if i == "owner":
                            action["amount"] = int(rental_price-commission)
                        elif i == "insurance":
                            action["amount"] = insurance
                        elif i == "assistance":
                            action["amount"] = assistance
                        else:
                            action["amount"] = drivy
                    rental["actions"].append(action)


                rentals_list["rentals"].append(rental)

with open("output.json", "w") as output_file:
    json.dump(rentals_list, output_file, indent=4)
