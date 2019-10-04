

from function import *

rentals = [] #Liste pour les resultats
with open('input.json') as json_file:
    data = json.load(json_file)
    #print(data)
    for y in data["rentals"]:
        for x in data["cars"]:
            if x["id"]==y["car_id"]:
                start_date = y["start_date"]
                end_date = y["end_date"]
                number_of_days = number_of_day(start_date, end_date)

                time_component = x["price_per_day"]*number_of_days
                distance_component = y["distance"]*x["price_per_km"]
                rental_price = time_component + distance_component
                print(rental_price)

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
