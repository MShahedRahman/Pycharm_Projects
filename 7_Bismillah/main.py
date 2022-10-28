from numpy import *

arr1 = array ([
                [1,2,3,4,5,6],
                [4,5,6,7,8,9]
              ])
print (arr1.ndim)
print (arr1.shape)
print (arr1.size)

arr2 = arr1.flatten()
print (arr2)

arr3 = arr2.reshape(2,2,3)
print (arr3)

m = matrix (arr1)
print (m)

mat = matrix ('1 2 3 ; 4 5 6; 7 8 9')
print (mat)

print (diagonal(mat))
print (mat.min())
print (mat.max())

mat1 = matrix ('1 2 3 ; 6 4 5 ; 1 6 7')
mat2 = matrix ('1 2 3 ; 6 8 5 ; 2 6 7')

mat3 = mat1 + mat2
mat4 = mat1 * mat2

print (mat3)
print (mat4)


