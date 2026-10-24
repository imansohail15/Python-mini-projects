def factorial(a):
    fact=1
    i=a
    while i>0:
        fact=fact*i
        i=i-1
    return fact
print(factorial(5))