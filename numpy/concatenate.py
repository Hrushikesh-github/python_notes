import numpy as np

a = np.zeros([4, 4])
b = np.ones([4, 4])
print(a)
print(b)

#use np.concatenate and tune the axis, 0 for row and 1 for column 


#vertical stacking equivalents(ROW WISE)
#np.concatenate([a, b], axis=0)
#np.vstack([a,b])
print(np.r_[a,b])
print(type(np.r_[a,b]))#<class 'numpy.ndarray'>


# Horizontal Stack Equivalents (Coliumn wise)
#np.concatenate([a, b], axis=1)
#np.hstack([a,b])
print(np.c_[a,b])

#leave this part
#################
#when arrays are 1d
print(np.r_[[1,2,3],0,0,[4,5,6]])
print(np.r_[[1,2,3],[4,5,6]])
#print(np.vstack([[1,2,3],0,0,[4,5,6]])) #would give error
print(np.vstack([[1,2,3],[4,5,6]]))


'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
<class 'numpy.ndarray'>
[[0. 0. 0. 0. 1. 1. 1. 1.]
 [0. 0. 0. 0. 1. 1. 1. 1.]
 [0. 0. 0. 0. 1. 1. 1. 1.]
 [0. 0. 0. 0. 1. 1. 1. 1.]]
[1 2 3 0 0 4 5 6]
[1 2 3 4 5 6]
[[1 2 3]
 [4 5 6]]

'''
