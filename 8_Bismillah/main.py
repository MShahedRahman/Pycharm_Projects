def add_sum(a,*b):
    print(a)
    print(b)

    c = a
    for i in b:
      c = c+i
    print(c)

add_sum(5,6,34,78)

def person(name, **data):
    print (name)
    for i,j in data.items():
        print(i,j)


person('Shahed', age= 33, city= 'Dhaka', mobile= '01749701317')

a=10
print (id(a))
def something():
    #global a
    a=15
    x= globals()['a']
    print(id(x))
    #print(id(a))
    print("Inside : ", a)
    globals()['a']=15

print("Outside : ",a)
something()

