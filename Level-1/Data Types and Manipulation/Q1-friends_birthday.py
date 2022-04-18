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