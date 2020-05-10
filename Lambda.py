#lambda functions used when we reuire a nameless function for a short period of time

# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

#it is used along with filter and map function

# Program to filter out only the even items from a list
#filter function takes a function(which returns a bool) and a list 
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
