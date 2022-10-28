from array import *

value1 = array('i', [5,7,9,3,4,5])
newArr = array(value1.typecode, (a*a for a in value1))


for i in newArr:
    print(i)

