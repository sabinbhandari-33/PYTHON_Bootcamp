# TO print fibonacci series of the designated number
n = int(input("Enter a number"))
def fibo(n):
    if n <= 1:
        return n
    else :
        return fibo(n-1) + fibo(n-2)

print("Fibonacci series")
for i in range(n):
    print(fibo(i))
