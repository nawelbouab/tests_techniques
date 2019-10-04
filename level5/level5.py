
from function import *

rentals_list = dict()
rentals_list["rentals"] = []

with open("input.json") as json_file:
    data = json.load(json_file)
    #print(data)
    for y in data["rentals"]:
        price_gps = 0
        price_baby_seat = 0
        price_addi_insurance = 0
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

                rental = OrderedDict()
                rental["id"] = y["id"]
                rental["options"] = []
                rental["actions"] = []

                for z in data["options"]:
                    if y["id"]==z["rental_id"]:
                        option = dict()
                        option = z["type"]
                        if z["type"] == "gps":
                            price_gps = number_of_days*500
                        if z["type"] == "baby_seat":
                            price_baby_seat = number_of_days*200
                        if z["type"] == "additional_insurance":
                            price_addi_insurance = number_of_days*1000
                        rental["options"].append(option)

                rental_price_with_options = rental_price + price_gps + price_baby_seat + price_addi_insurance

                for i in ["driver", "owner", "insurance", "assistance", "drivy"]:
                    action = OrderedDict()
                    action["who"] = i
                    if i == "driver":
                        action["type"] = "debit"
                        action["amount"] = rental_price_with_options
                    else:
                        action["type"] = "credit"
                        if i == "owner":
                            action["amount"] = int(rental_price-commission+price_gps+price_baby_seat)
                        elif i == "insurance":
                            action["amount"] = insurance
                        elif i == "assistance":
                            action["amount"] = assistance
                        else:
                            action["amount"] = drivy + price_addi_insurance
                    rental["actions"].append(action)



                rentals_list["rentals"].append(rental)

with open("output.json", "w") as output_file:
    json.dump(rentals_list, output_file, indent=4)
