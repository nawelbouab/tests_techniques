
from function import *

#Initialisation du dictionnaire principal
rentals_list = dict()
rentals_list["rentals"] = []
with open('input.json') as json_file:
    data = json.load(json_file)
    for y in data["rentals"]:
        for x in data["cars"]:
            if x["id"]==y["car_id"]:
                start_date = y["start_date"]
                end_date = y["end_date"]
                number_of_days = number_of_day(start_date, end_date)

                price_per_day=x["price_per_day"]
                distance_component = y["distance"]*x["price_per_km"]
                rental_price = int(distance_component) + time_compo(number_of_days, price_per_day)


                #Calcul des commissions
                commission = rental_price*0.3
                insurance = commission/2
                assistance = number_of_days*100
                drivy = commission - insurance - assistance

                #Creation du dictionnaire pour les commissions
                commission_dict = dict()
                commission_dict["insurance_fee"] = int(insurance)
                commission_dict["assistance_fee"] = int(assistance)
                commission_dict["drivy_fee"] = int(drivy)

                #Creation du dictionnaire de la location
                rental = OrderedDict()
                rental["id"] = y["id"]
                rental["price"] = int(rental_price)
                rental["commission"] = commission_dict

                #Ajout dans le dictionnaire principal
                rentals_list["rentals"].append(rental)


#Sauvegarde les resultats dans un JSON
with open('output.json', 'w') as output_file:
    json.dump(rentals_list, output_file, indent=4)
