class Stack:

    def __init__(self):

        self.__stackList = []



    def push(self, val):

        self.__stackList.append(val)



    def pop(self):

        val = self.__stackList[-1]

        del self.__stackList[-1]

        return val



#defining a subclass.It gets all components defined by its superclass

class AddingStack(Stack):
##we must explicitly invoke a superclass's constructor #invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list but here you have to point to the object, so thus used here
    def __init__(self):

        Stack.__init__(self)

        self.__sum = 0



    def getSum(self):

        return self.__sum



    def push(self, val):

        self.__sum += val

        Stack.push(self, val)



    def pop(self):

        val = Stack.pop(self)

        self.__sum -= val

        return val





stackObject = AddingStack()



for i in range(5):

    stackObject.push(i)

print(stackObject.getSum())



for i in range(5):

    print(stackObject.pop())
