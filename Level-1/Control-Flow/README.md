## Control Flow



##### ```1. What is the difference between 10 / 3 and 10 // 3?```

The answer to ```10 / 3 ``` is 3.3333333333333335 and ```10 // 3 ``` is 3.

``reason: ``

```//``` is the floor division operator which divides and rounds the value to the nearest integer.

while ```/``` is plain old division operator.


#### ```2. What is the result of 10 ** 3?```

answer: The result of 10^3 is ``1000``.


#### ```3. Given (x = 1), what will be the value of after we run (x += 2)?```

answer: ```3```


#### ```4. How can we round a number?```

answer: We can use python built-in function ```round``` 
```
example: 
    x = 12.76543
    print(round(x)) // 13

    we can also specify to round the number upto n number of decimal points.

    print(round(x, 2)) // 12.77

```

#### ```5. What is the result of float(1)?```

answer: The ``float`` method returns a floating point number in this case the answer would be ```1.0```.


#### ```6. What is the result of bool(“False”)?```

answer: The ``bool`` method converts the given value to a boolean. So In our case the value is in string format that has the value ```"False"``` which is ``True``.
        If an ```""``` empty string is passed it returns ``False``.


#### ```7. What are the falsy values in Python?```

answer: None, False, zero of any numeric type: 0, 0L, 0.0, 0j, empty sequences and collections: ```[], {}, (), '', b'', set(), empty range, like range(0)```,


#### ```8. What is the result of 10 == “10”?```

answer: This results in ```False```. Blame type-casting.


#### ```9. What is the result of “bag” > “apple”?```

answer: The answer to this is ```True```. The reason for this is ```string lexicographically```.


#### ```10. What is the result of not(True or False)?```

answer: The answer to this is ```False```.


#### ```11. Under what circumstances does the expression 18 <= age < 65 evaluate to True?```

answer: For values greater than or equal to 18 and less than 65.


#### ```12. What does range(1, 10, 2) return?```

answer: It will return 

```
1
3
5
7
9
```

for the following code: 
```
x = range(1, 10, 2)

for n in x:
  print(n)
```

The reason for this is that the range() funcion ```2 optional``` and ```1 required parameter```

The first paramater is the ```start``` of the position at which we start. [by default it is 0]
The second one is the ```stop``` parameter specifying where to stop [REQUIRED]
The third parameter is the ```step``` that specify the increment. [by default it is one].


#### ```13. Name 3 iterable objects in Python.```

answer: Lists, tuples, dictionaries, and sets are all iterable objects.