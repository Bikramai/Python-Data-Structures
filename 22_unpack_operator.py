numbers = [1, 2, 3]
print(numbers)
print('\n')

numbers = [1, 2, 3]
print(*numbers) #unpacking operator (...numbers in javascript)
print('\n')

values = list(range(5))
values = [*range(5), *'Hello'] #unpack any iterable and stings
print(values)
print('\n')

# unpack using operator we can combine with more than two list 
first = [1, 2]
second = [3]
values = [*first, 'a', *second, *'Hello']
print(values)

# we can also unpack dictionaries
first = {'x': 1}
second = {'x': 10, 'y': 2}
combined = {**first, **second, 'z': 1} #unpack and add 
print(combined)

