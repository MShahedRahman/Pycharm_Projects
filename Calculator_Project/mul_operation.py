def mul(a,b):
    return a*b

def mul_operation():
    counter = int(input("How many numbers you want to multiply: "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the next number: "))
    for i in range(counter-1):
        mul_result = mul(a, b)
        a = mul_result
        if i == counter-2:
            continue
        else:
            b = int(input("Enter the next number: "))
    print("The final result is : ", mul_result)