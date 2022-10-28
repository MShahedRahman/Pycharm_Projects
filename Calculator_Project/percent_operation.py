def percentage(a,b):
    return (b * 100)/a

def percent_operation():
    a = int(input("Enter the principal number : "))
    b = int(input("Enter the percentage you want to determine : "))
    per_result = percentage(a, b)
    print("The final result is : ", per_result,"%")