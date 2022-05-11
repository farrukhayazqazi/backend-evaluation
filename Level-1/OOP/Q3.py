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


    

    
    print('TOTAL ITEMS: ', items_count)
    
    
    

class ListBox(Box):

  def __init__(self):
    self.items = []

  def add(self, item):
      self.items.append(item)
  
  def empty(self):
      self.items.clear()
  
  def count(self):
      return len(self.items)


class DictBox(Box):
    def __init__(self):
      self.items = {}

    def add(self, item):
        self.items[item] = item
    
    def empty(self):
        self.items.clear()
    
    def count(self):
        return len(self.items)

list_box1 = ListBox()
dict_box = DictBox()
list_box2 = ListBox()


for n in range(20):
    list_box1.add(f"item {n}")


for n in range(5):
    dict_box.add(f"item {n}")

for n in range(9):
    list_box2.add(f"item {n}")

repack_boxes(list_box1, dict_box, list_box2)
for index, box in enumerate([list_box1, dict_box, list_box2]):
    print(f'box {index+1} length: ', box.count())


