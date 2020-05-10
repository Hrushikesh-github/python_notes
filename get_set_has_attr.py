class Person:
    age = 23
    name = 'Adam'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
#The hasattr() method returns true if an object has the given named attribute and false if it does not.
#hasattr(object, name)
print('Person age is', getattr(person,'age'))
setattr(person,'gender','male')
print("gender is ",getattr(person,'gender'))
print(person.gender)
