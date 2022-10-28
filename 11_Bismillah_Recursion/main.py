from _functools import *

nums = [2,3,4,5,6,8,7,9,10]

even = list(filter(lambda a: a%2==0, nums))
print (even)

doubles = list (map(lambda b: b*2,even))
print (doubles)

sum = reduce(lambda a, b: a+b, doubles)
print (sum)



