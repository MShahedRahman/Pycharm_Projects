def sub(a,b):
    return a-b

def sub_operation():
    counter = int(input("How many numbers you want to subtract: "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the next number: "))
    for i in range(counter-1):
        sub_result = sub(a, b)
        a = sub_result
        if i == counter-2:
            continue
        else:
            b = int(input("Enter the next number: "))
    print("The final result is : ", sub_result)