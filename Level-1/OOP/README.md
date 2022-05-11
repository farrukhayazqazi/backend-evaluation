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


###### 2. Write an “abstract” class, Box, and use it to define some methods which any box object should have: add, for adding any number of items to the box, empty, for taking all the items out of the box and returning them as a list, and count, for counting the items which are currently in the box. Write a simple Item the class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.

```
from abc import ABC, abstractmethod

class Box(ABC):

    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass


class Item:
     def __init__ (self, name, value):
        self.name = name
        self.value = value

class ListBox(Box):

    items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} added to the items list.")
    
    def empty(self):
        self.items.clear()
        print("items list emptied.")
    
    def count(self):
        print(f"{len(self.items)} items in items list")


class DictBox(Box):
    items = {}

    def add(self, item):
        self.items[item] = item
        print(f"{item} added to the items dict.")
    
    def empty(self):
        self.items.clear()
        print("items dict emptied.")
    
    def count(self):
        print(f"{len(self.items)} items in items dict")

list_box = ListBox()
dict_box = DictBox()

list_box.add('sanitizer')
dict_box.add('apple')

list_box.empty()

dict_box.count()
list_box.count()


```

###### 3. Extending question 2 of this section, Write a function, repack_boxes, which takes any number of boxes as parameters, gathers up all the items they contain, and redistributes them as evenly as possible over all the boxes. Order is unimportant. There are multiple ways of doing this. Test your code a ListBox with 20 items, a ListBox with 9 items and a DictBox with 5 items. You should end up with two boxes with 11 items each, and one box with 12 items.

```
def repack_boxes(*boxes):

    total_boxes = len(boxes)
    items_count = 0
    avg_count = 0
    total_items = []
    
    for box in boxes:
        items_count += box.count()
        for item in box.items:
            total_items.append(item)
            
    avg_count = int(items_count/total_boxes)
    
    for box in boxes:
        box.empty()
        while(True):
            if (box.count() != avg_count and len(total_items)):
                box.add(total_items.pop(0))
            else:
                break
    
    # adding remaining items in last box
    for item in total_items:
        boxes[len(boxes)-1].add(item)

```