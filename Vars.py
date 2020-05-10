class TempClass:
    def __init__(self):
        self.b=2
        self.c=3
        d=4
    a = 1
    def temp_function(self):
        pass

print(TempClass.__dict__)
d=TempClass()
print(vars(d))
##Also used in argparse
#vars() takes a maximum of one parameter.
#object - can be module, class, instance, or any object having the __dict__ attribute.
#class variables aren't shown in an object's __dict__
