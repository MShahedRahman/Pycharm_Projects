import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
symbols = "(){}[]!@#$%&\|/*^;,._-"

upper, lower, nums, symbs = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if symbs:
    all += symbols

length = 20
amount = 10

seed = "myPassword" # for always having the same combination of password
random.seed(seed)  # for always having the same combination of password

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

