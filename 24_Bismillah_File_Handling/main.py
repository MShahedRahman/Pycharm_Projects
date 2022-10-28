

f = open('MyData','a')

f1 = open('abc', 'r')

for data in f1:
    print(data)
    f.write(data)

