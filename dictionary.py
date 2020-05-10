dict={"cat":"pilli","dog":"kuka","horse":"gurram"}#key->value
dict['tiger']='simham' #add or create in this way by initiazling dict={}
print(dict)
del dict['cat']#both value and keys are lost
print('tiger' in dict)#in and not in also used in lists,tuples
##############
for animal in dict.keys():
    print(animal,"->",dict[animal])
for jenthu in dict.values():
    print(jenthu)#dictionary cannot find key for a given value
for animal,jenthu in dict.items():
    print(animal,"==",jenthu)
for AA in dict.items():
    print(AA)
print("length of dictinoary is:", len(dict))
print("output when u print dict is:",dict)
print("output when u use sorted before dict is:",sorted(dict))
print(dict.get('tiger') #using get gives none when no key is present
        
'''
Another example
d={}
d['2']=[1,2]
d['1']=[3,4]
print(d)

for x in d.keys():
    print(d[x][1], end="")
'''
{'2': [1, 2], '1': [3, 4]}
24
'''
'''
        
'''
{'cat': 'pilli', 'dog': 'kuka', 'horse': 'gurram', 'tiger': 'simham'}
True
dog -> kuka
horse -> gurram
tiger -> simham
kuka
gurram
simham
dog == kuka
horse == gurram
tiger == simham
('dog', 'kuka')
('horse', 'gurram')
('tiger', 'simham')

'''
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

'''
The get() method returns:

the value for the specified key if key is in dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.
Name:  Phill
Age:  22
Salary:  None
Salary:  0.0
'''
'''
>>> model={'heads':0.2,'tails':0.8}
>>> a=model.keys
>>> a
<built-in method keys of dict object at 0x7f6786d1b630>
>>> type(a)
<class 'builtin_function_or_method'>
>>> print(a)
<built-in method keys of dict object at 0x7f6786d1b630>
>>> a=model.keys()
>>> print(a)
dict_keys(['heads', 'tails'])
>>> type(a)
<class 'dict_keys'>
>>> a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_keys' object does not support indexing
>>> for i in a:
...     print(i)
...
heads
tails
>>> type(i)
<class 'str'>
'''
