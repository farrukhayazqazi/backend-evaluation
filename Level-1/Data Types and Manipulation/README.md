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
        'whis': '2 July',
        'gohan': '9 Jan'
    }
    return friends_birthdays[name.lower()]

print(get_birthdays())
```