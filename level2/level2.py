
from function import *

rentals = [] #Liste pour les resultats
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

                #Ajoute le calcul a la liste
                dico=OrderedDict()
                dico['id']=y['id']
                dico['price']= int(rental_price)
                rentals.append(dico)

#Ajoute la liste dans un dictionnaire
result = {
    'rentals': rentals,
}
#Sauvegarde les resultats dans un JSON
with open('output.json', 'w') as output_file:
    json.dump(result, output_file, indent=4)
