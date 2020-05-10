#! /usr/ein/env python
print("Hello {0},your balance is {1:0.3f}".format("Adam",23.478))
#The curly braces are just placeholders for the arguments to be placed. In the above example, {0} is placeholder for "Adam" and {1:9.3f} is placeholder for 230.2346.
#Since "Adam" is the 0th argument, it is placed in place of {0}. Since, {0} doesn't contain any other format codes, it doesn't perform any other operations.
#However, it is not the case for 1st argument 230.2346. Here, {1:9.3f} places 230.2346 in its place and performs the operation 9.3f.
#f is for float number, and part after '.' (3) truncates decimal to 3 places. and part before '.' place a high number like 30 and u will see what happens. 
#generally .3 is used no need for part before '.'.
