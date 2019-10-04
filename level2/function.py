import json
from datetime import datetime
from collections import OrderedDict

def time_compo(num_days, price_day):
    time_component=0
    if num_days>10:
        time_component=(num_days-10)*0.5*price_day+6*0.7*price_day+3*0.9*price_day+1*price_day
    elif num_days>4:
        time_component=(num_days-4)*0.7*price_day+3*0.9*price_day+1*price_day
    elif num_days>1:
        time_component=(num_days-1)*0.9*price_day+1*price_day
    else:
        time_component=price_day

    return time_component

def number_of_day(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    return abs((end_date - start_date).days)+1
