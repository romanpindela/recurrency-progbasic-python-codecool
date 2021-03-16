count = []
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        count.append(x) 
        print(x)    
        return (x * factorial(x-1))



num = 10
print("The factorial of", num, "is", factorial(num))
print(count)