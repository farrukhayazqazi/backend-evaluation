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