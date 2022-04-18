## Functions:

###### 1. Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

```
def generateFibonacci():
    num = int(input('How many Fibonacci numbers to generate? : '));
    nth = 0
    n1 = 0
    n2 = 1
    fibArray = [] 
    while (num != len(fibArray)):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fibArray.append(n1)
    print(fibArray)
        
print(generateFibonacci())

```
###### 2. What is the difference between a parameter and an argument?

**parameters** are the placeholders that we declare at the time of defining a function.
 An **argument** is the actual value that is passed to that function.

```
// for example

def function(param1, param2):   // these are parameters
    return param1 + param2

function(2, 3)   // these are arguments
```

###### 3. All functions in Python by default return …?

All functions in python return the value **None** if any explicit return value is not provided

###### 4. What are keyword arguments and when should we use them?

Keyword arguments are passed with their specific parameter names. 

Why should one use them?

Unlike positional arguments, keyword arguments doesn't have to do anything with the position of the argument, all that matters is that you have the right parameter name for the right argument.

###### 5. How can we make a parameter of a function optional?

We can use **optional arguments** that has a default value. We can specify the default value at the time of defining the function. So if that optional argument is not provided at the time of passing argument that optional argument will use the default value instead.

```
// for example

def greet_user(name, text=', Welcome to Hirecinch!'):    // _text_ has the default value
    return name + text

print(greet_user('Farrukh Ayaz'))       // here if we do not pass the text argument value it will use the default value.
```
we can use ***args** if we want to pass any arbitirary number of arguments (to perform operations on a tuple) and similary we can pass ****kwargs** for keyword arguments (to perform actions on a dictionary).


###### 6. What happens when we prefix a parameter with an asterisk (*)?

if we prefix a parameter with an asterisk (*), essentially what that means is that we are setting the parameter to recieve an arbitarary number of arguments that can be used as a tuple to perform operations on it and they are represented by ***args**
 (are optional).

```
// for example

def check(*args):
    return f'This is an optional positional argument as a tuple {args}'
    
print(check('arg'))
```

###### 7. What about two asterisks (**)?

if we prefix a parameter with two asterisks (**), this means that we are setting the parameter to recieve an arbitarary number of keyword arguments that can be used as a dictionary to perform operations on and they are represented by ****kwargs**
 (are optional).

```
// for example

def check(**kwargs):
    return f'This is an optional keyword argument as a dictionary {kwargs}'

bio = {
    'name': 'Farrukh Ayaz',
    'age': '23',
}
    
print(check(myself=bio))
```

###### 8. Write a function that prints all the prime numbers between 0 and limit where the limit is a parameter.

```
limit=int(input("Enter limit: "))
for is_prime_number in range (2, limit+1):
    for dividend in range(2, is_prime_number):
        if is_prime_number%dividend == 0:
            break
    else:
        print(is_prime_number)
```