import json
from datetime import datetime

rentals = [] #Liste pour les resultats
with open('input.json') as json_file:
    data = json.load(json_file)

for rental in data["rentals"]:
    for car in data["cars"]:
        if car["id"] == rental["car_id"]:
            d1 = datetime.strptime(rental["start_date"], "%Y-%m-%d")
            d2 = datetime.strptime(rental["end_date"], "%Y-%m-%d")
            time_component = car["price_per_day"] * (abs((d2 - d1).days)+1)
            distance_component = car["price_per_km"] * rental["distance"]
            rental_price = time_component + distance_component
            print(rental_price)
            #Ajoute le calcul a la liste
            rentals.append({
                'id': rental['id'],
                'price': rental_price,
            })

#Ajoute la liste dans un dictionnaire
result = {
    'rentals': rentals,
}
#Sauvegarde les resultats dans un JSON
with open('output.json', 'w') as output_file:
    json.dump(result, output_file, indent=4)
