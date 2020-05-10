import numpy as np
#ap.arange to create customised # sequences as ndarray

print(np.arange(5))# lower limit is 0 by default
print(np.arange(10,0,-2))


#random module provides nice functions

print(np.random.rand(2,2)) 
#random # between [0,1) of shape 2,2

print(np.random.randn(2,2))
# Normal distribution with mean=0 and variance=1 of shape 2,2
print(np.random.randint(0,10,size=[2,2]))   
#random integes between [0,10) of shape 2,2

# One random number between [0,1)
print(np.random.random())

# Random numbers between [0,1) of shape 2,2
print(np.random.random(size=[2,2]))

# Pick 10 items from a given list, with equal probability
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

# Pick 10 items from a given list with a predefined probability 'p'
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10, p=[0.3, .1, 0.1, 0.4, 0.1]))  # picks more o's
'''
[0 1 2 3 4]
[10  8  6  4  2]
[[0.4025376  0.67378262]
 [0.75014973 0.91319589]]
[[-0.85527227 -0.50835318]
 [ 0.40439    -1.08638622]]
[[1 1]
 [9 0]]
0.38198558631291246
[[0.63354053 0.06683765]
 [0.39968914 0.549172  ]]
['a' 'e' 'e' 'a' 'o' 'e' 'u' 'i' 'e' 'o']
['o' 'a' 'o' 'a' 'o' 'o' 'o' 'u' 'o' 'a']

'''

np.random.seed(100)

# Create random numbers between [0,1) of shape 2,2
print(np.random.rand(2,2))

# [[ 0.54  0.28]
#  [ 0.42  0.84]]

'''
>>> np.random.permutation(10)
array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6])
>>> np.random.permutation([1, 4, 9, 12, 15])
array([15,  1,  9,  4, 12])
Randomly permute a sequence, or return a permuted range.
If x is a multi-dimensional array, it is only shuffled along its first index.
'''

print(np.linspace(1,10,5))
#Return evenly spaced numbers over a specified interval.

