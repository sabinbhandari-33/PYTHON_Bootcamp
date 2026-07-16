# TO check if a number is prime or not
a = int(input("enter a number"))
if a<=1:
    print( a, "is neither a prime nor a composite number.")
else:
    for i in range(2, a):
        if a % i == 0:
            print(a, "is not a Prime Number")
            break
    else:
        print(a, "is a Prime Number")
