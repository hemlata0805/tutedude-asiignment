#task 1:
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

num=5
print("Factorial of",num,"is: ",factorial(num))

#task 2:
from math import *

number=int(input("Enter a number: "))
print("Square root: ",sqrt(number))
print("logarithm: ",log(number))
print("Sine: ",sin(number))