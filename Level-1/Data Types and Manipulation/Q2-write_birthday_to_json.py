import json

with open('Q2-json.json') as json_file:
    dictionary = json.load(json_file)

def get_birthdays():
    name = input("Enter the name of the saiyan: \n")
    birthday = input("Enter the birthday of the saiyan: \n")
    dictionary['data']['friends_birthdays'][name] = birthday
    json_file = open('Q2-json.json', 'w')
    json.dump(dictionary, json_file, indent=2)
    json_file.close()

get_birthdays()