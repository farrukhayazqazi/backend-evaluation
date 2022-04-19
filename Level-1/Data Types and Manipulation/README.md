## Data types and Manipulation:

###### 1. We will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name and return the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin

```
def get_birthdays():
    name = input("Who's birthday do you want to look up?\n")
    friends_birthdays = {
        'goku': '24 March',
        'vegeta': '1 April',
        'broly': '2 July',
        'gohan': '9 Jan'
    }
    return friends_birthdays[name.lower()]

print(get_birthdays())
```

###### 2. Modify your program from Question 1 of this section to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program. Finally, ask the user for another super sayain’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

```
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
```

###### 3. We saved information about famous saiyans’ names and birthdays to disk. Now we load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month. (Hint: Use counter from the collections module.)
Your program should output something like:
``{"May": 3,"November": 2,"December": 1}``

```
import json
from collections import Counter


with open ('Q2-json.json') as json_file:
    json = json.load(json_file) 

    months = []
    for birthday in json['data']['friends_birthdays'].values():
        months.append(birthday.split(' ')[1])

    counter = Counter(months)
    print(dict(counter))
```