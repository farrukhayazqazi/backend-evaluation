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


