def factorial(n):
    result =1
    for i in range(n,1,-1):
        result = i * result
    return result

i = int(input("Enter a number : "))
print("The factorial of the number", i, "is: ", factorial(i))

def factorial_1(n):
    if n==0:
        return 1
    else:
        return n * factorial_1(n - 1)

result = factorial_1(5)
print(result)