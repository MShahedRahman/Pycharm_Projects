
a = 5
b = 2


try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You can not divide a Number by zero.", e)

except ValueError as v:
    print("Invalid Input,", v)

except Exception as all:
    print("Something went wrong")

finally:
    print("Resource Close")

print("Bye")