import json
from collections import Counter


with open ('Q2-json.json') as json_file:
    json = json.load(json_file) 

    months = []
    for birthday in json['data']['friends_birthdays'].values():
        months.append(birthday.split(' ')[1])

    counter = Counter(months)
    print(dict(counter))

