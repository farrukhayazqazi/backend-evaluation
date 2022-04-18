limit=int(input("Enter limit: "))
for is_prime_number in range (2, limit+1):
    for dividend in range(2, is_prime_number):
        if is_prime_number%dividend == 0:
            break
    else:
        print(is_prime_number)