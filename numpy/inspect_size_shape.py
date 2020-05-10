import numpy as np

list2 = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
arr2 = np.array(list2, dtype='float')

print(arr2)
print('Shape:', arr2.shape)
print('Datatype:', arr2.dtype)
print('Size:', arr2.size)
print('Num Dimensions:', arr2.ndim)

print(arr2[:2,:2]) #extract 1st 2 rows and columns
#it's square brackets like lists

#boolean indexing
b=arr2>4
print(b)

print(arr2[b])
arr2[arr2>4]=0
arr2[arr2<0]=1
print(arr2)

'''
[[1. 2. 3. 4.]
 [3. 4. 5. 6.]
 [5. 6. 7. 8.]]
Shape: (3, 4)
Datatype: float64
Size: 12
Num Dimensions: 2
[[1. 2.]
 [3. 4.]]
[[False False False False]
 [False False  True  True]
 [ True  True  True  True]]
[5. 6. 5. 6. 7. 8.]
[[1. 2. 3. 4.]
 [3. 4. 0. 0.]
 [0. 0. 0. 0.]]
'''

arr2a=arr2[:2, :2] #assign portion of arr2 to arr2a. Doesn't create a new array
arr2a[:1,:1]=100 #100 will reflect in arr2

print(arr2)
print(arr2a)
'''
[[100.   2.   3.   4.]
 [  3.   4.   5.   6.]
 [  5.   6.   7.   8.]]
[[100.   2.]
 [  3.   4.]]

'''

arr2b=arr2[:2,:2].copy()
arr2b[:1,:1]=101
print(arr2)
print(arr2b)
'''
[[100.   2.   3.   4.]
 [  3.   4.   5.   6.]
 [  5.   6.   7.   8.]]
[[101.   2.]
 [  3.   4.]]

'''

# reshape a 3*4 array to 4*3
arr2.reshape(4,3)
print(arr2)
#Flattening is to make it 1d array
print(arr2.flatten())
#note that change in flatten array does not affect parent array!!
'''
[[100.   2.   3.   4.]
 [  3.   4.   5.   6.]
 [  5.   6.   7.   8.]]
[100.   2.   3.   4.   3.   4.   5.   6.   5.   6.   7.   8.]

'''

