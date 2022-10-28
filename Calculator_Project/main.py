from add_operation import *
from sub_operation import *
from mul_operation import *
from div_operation import *
from percent_operation import *

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Percentage Operation")

operation = int (input("Select an Operator to Perform: "))

if operation == 1:
    print("You have chosen Add Operation")
    add_operation()
elif operation == 2:
    print("You have chosen Subtract Operation")
    sub_operation()
elif operation == 3:
    print("You have chosen Multiply Operation")
    mul_operation()
elif operation == 4:
    print("You have chosen Divide Operation")
    div_operation()
elif operation == 5:
    print("You have chosen Percentage Operation")
    percent_operation()
else:
    print("Invalid Input")


