n = int(input("Enter a number: "))
def factorial(n):
    s = 1
    if n == 0:
        print("Factorial of", n , "is:",1)
    elif n == 1:
        print("Factorial of", n , "is:",1)
    else:
        n > 2
        for i in range(1,n+1):
            s = s*i
        print("Factorial of",n,"is:",s)

factorial(n)

