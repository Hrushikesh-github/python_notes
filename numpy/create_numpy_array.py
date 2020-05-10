import numpy as np
list1=[0,1,2,3,4]
print(type(list1))
#<class 'list'>
arr1d=np.array(list1) #create array
print(type(arr1d))
#<class 'numpy.ndarray'>

#list1 + 2 -> will give error
print(arr1d+2) # add all elements by 2

#Also you can specify datatype

list2=[[0,1,2],[3,4,5],[6,7,8]]
arr2d=np.array(list2)
print(arr2d)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
arr2d_f=np.array(list2, dtype='float')
print(arr2d_f)
'''
[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]
'''
#u can also converet to diff datatypes
print(arr2d==arr2d_f.astype("int"))
'''
[[ True  True  True]
 [ True  True  True]
 [ True  True  True]]

'''

# u can convert np.array to list using tolist()

>>> W=np.array([(2,1),(3,7)])
>>> W
array([[2, 1],
       [3, 7]])

