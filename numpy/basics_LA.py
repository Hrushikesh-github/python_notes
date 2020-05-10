import numpy as np
from math import inf
a=np.array([1,2,3])
print(a)

l1=np.linalg.norm(a,1)
print("L1 norm is:",l1)
l2=np.linalg.norm(a)
print("L2 norm is:",l2)
maxnorm=np.linalg.norm(a,inf)
print("max norm is:",maxnorm)


