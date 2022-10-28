import numpy as np

print(np.zeros(10, dtype='float'))
print(np.ones((3,5), dtype= 'int'))
print(np.ones(10, dtype= 'int'))
print(np.full((2,5), 2))
print(np.arange(0, 20, 2))
print(np.linspace(1, 10, 5))
print(np.random.normal(0, 1, (3,3)))
print(np.eye(4))

x1 = np.array([1,2,3,4,5,6,7,8,9])
print(x1)
print(x1[::-1]) #Reversing_the_array
print(x1[2])
print(x1[-2])

x2 = np.random.randint(10, size=(3,4))
print(x2)
print(x2[2,1])
print(x2[2,-1])

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [21,21,21]
print(np.concatenate([x, y,z]))