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

###### Modify your program from Question 1 of this section to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program. Finally, ask the user for another super sayain’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

```

```