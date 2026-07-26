n = int(input("Enter a number"))
def fact(n):
    if n==0 or n==1:
        return(1)
    else:
        return n * fact(n-1)
print("The factorial is", fact(n))
