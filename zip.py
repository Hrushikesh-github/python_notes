#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
#we can then run them in a for loop
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)
print("result without using set",result)
# Converting to set
result_set = set(result)
a,b=result_set
c,d,e=zip(*result_set)
print("a is",a)
print("b is",b)
print("c is",c)
print("d is",d)
print("e is",e)
print(result_set)
'''
{(3, 'THREE'), (1, 'ONE'), (2, 'TWO')}
result without using set <zip object at 0x7fe960c0c308>
a is (1, 'one', 'ONE')
b is (2, 'two', 'TWO')
c is (1, 2)
d is ('one', 'two')
e is ('ONE', 'TWO')
{(1, 'one', 'ONE'), (2, 'two', 'TWO')}

'''

import numpy as np

X= np.array([[0,10],[1,11],[2,12],[3,13]])
y=np.array([[0],[1],[2],[3]])#our target


print("our 1st matrix is:",X)
print("our y matrix was:",y)
print(y.shape)
print(X.shape)

for (x,target) in zip(X,y):
    print("our 1st matrix goes like:",x)
    print("and the target is:",target)
'''
('our 1st matrix is:', array([[ 0, 10],
       [ 1, 11],
       [ 2, 12],
       [ 3, 13]]))
('our y matrix was:', array([[0],
       [1],
       [2],
       [3]]))
(4, 1)
(4, 2)
('our 1st matrix goes like:', array([ 0, 10]))
('and the target is:', array([0]))
('our 1st matrix goes like:', array([ 1, 11]))
('and the target is:', array([1]))
('our 1st matrix goes like:', array([ 2, 12]))
('and the target is:', array([2]))
('our 1st matrix goes like:', array([ 3, 13]))
('and the target is:', array([3]))

'''



