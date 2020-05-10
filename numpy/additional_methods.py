import numpy as np
A=["hel","ana","cdd","ana","hel","zomb"]
B=np.unique(A)
print(B)
#array(['ana', 'cdd', 'hel', 'zomb'], dtype='<U4')
print(B[0])
#'ana'
print(type(B[0]))
#<class 'numpy.str_'>


