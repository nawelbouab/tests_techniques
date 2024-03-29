from function import *

rentals_list = dict()
rentals_list["rentals"] = []

with open("input.json") as json_file:
    data = json.load(json_file)
    #print(data)
    for y in data["rentals"]:
        for x in data["cars"]:
            if x["id"]==y["car_id"]:
                start_date = y["start_date"]
                end_date = y["end_date"]
                number_of_days = number_of_day(start_date, end_date)

                price_per_day=x["price_per_day"]
                distance_component = y["distance"]*x["price_per_km"]
                rental_price = int(distance_component) + time_compo(number_of_days, price_per_day)


                commission = rental_price*0.3
                insurance = int(commission/2)
                assistance = number_of_days*100
                drivy = int(commission - insurance - assistance)


                rental = dict()
                rental["id"] = y["id"]
                rental["actions"] = []

                for i in ["driver", "owner", "insurance", "assistance", "drivy"]:
                    action = OrderedDict()
                    action["who"] = i
                    if i == "driver":
                        action["type"] = "debit"
                        action["amount"] = int(rental_price)
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
