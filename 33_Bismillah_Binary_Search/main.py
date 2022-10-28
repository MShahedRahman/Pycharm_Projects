from math import *

pos = -1

def lin_search(list, val):
    lb = 0
    ub = len(list)

    for i in list:
        mb = floor((lb + ub) / 2)
        if list[mb] == val:
            globals()['pos'] = mb
            return True
        elif list[mb] <= val:
            lb = mb
            ub = ub
        elif list[mb] >= val:
            lb = lb
            ub = mb
    return False

list = [4,5,7,8,45,67,88,98,99]

n = 45

if lin_search(list, n):
    print("Found at : ", pos+1)
else:
    print("Not Found")



