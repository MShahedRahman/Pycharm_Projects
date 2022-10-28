def add(a,b):
    return a+b

def add_operation():
    counter = int(input("How many numbers you want to add: "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the next number: "))
    for i in range(counter-1):
        add_result = add(a, b)
        # print("The result is : ", add_result)
        a = add_result
        if i == counter-2:
            continue
        else:
            b = int(input("Enter the next number: "))
    print("The final result is : ", add_result)