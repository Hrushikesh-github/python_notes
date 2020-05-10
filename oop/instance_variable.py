class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def setSecond(self, val):
        self.second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)
'''
{'first': 1}
{'second': 3, 'first': 2}
{'third': 5, 'first': 4}
'''
#the class named ExampleClass has a constructor, which unconditionally creates an instance variable named first
#the class also has a method which creates another instance variable, named second
#exampleObject3 has been enriched with a property named third just on the fly, outside the class's code - this is possible and fully permissible.
#Python objects, when created, are gifted with a small set of predefined properties and methods. Each object has got them, whether you want them or not. One of them is a variable named __dict__ (it's a dictionary).
#The variable contains the names and values of all the properties (variables) the object is currently carrying. Let's make use of it to safely present an object's contents.
