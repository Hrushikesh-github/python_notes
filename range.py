# empty range
print(list(range(0)))

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))

start = 2
stop = 14
step = 2

print(list(range(start, stop, step)))

start = 2
stop = -14
step = -2

print(list(range(start, stop, step)))

# value constraint not met
print(list(range(start, 14, step)))

print(list(map(lambda x: x**2, range(10))))

'''
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 4, 6, 8, 10, 12]
[2, 0, -2, -4, -6, -8, -10, -12]
[]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
