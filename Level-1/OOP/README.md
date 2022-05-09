 ## OOP

 ###### 1. Write a simple program that loops over a list of user data (tuples containing a username, email, and age) and adds each user to a directory if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy that defines a different exception for each of these...

 ```
import re 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
validated_users = {}
user_data = [
    ("Goku", "supersaiyan@dbz.com", 15),
    ("Farrukh", "farrukhayaqazi@.faq.com", 23),
    ("Broly", "broly@dbz.com", 13),
    ]

# Check for valid email

def check(email):   
    if(re.search(regex,email)):   
        return False   
    else:   
        return True 


# Exceptions here

class DuplicateUserName(Exception):
    pass

class InvalidAge(Exception):
    pass

class Under16(Exception):
    pass

class InvalidEmail(Exception):
    pass




# base class

class User():
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age



# Checking cases

for data in user_data:
    user = {
    'username': data[0],
    'email': data[1],
    'age':data[2],
    }

    try:
        if user['username'] in validated_users:
            raise DuplicateUsername
        if user['age'] <= 0:
            raise InvalidAge
        if user['age'] < 16:
            raise Under16          
        if check(user['email']):
            raise InvalidEmail
    except DuplicateUserName:
        print('username should not be duplicate')
    except InvalidAge:
        print('invalid age')
    except Under16:
        print('user is under 16')
    except InvalidEmail:
        print('email address is not valid')
    
    validated_users[user['username']] = User(user['username'],user['email'], user['age'])
    
print(validated_users)

```