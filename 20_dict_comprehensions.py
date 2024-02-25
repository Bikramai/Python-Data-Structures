values = []
for x in range(5):
    values.append(x * 2)


#this a line of code is exactly idential to above 3 lines
# whenever you have above pattern of code we can use 
values = {x: x * 2 for x in range(5)}
print(values)

# instead of defining
values = {} # empty dict
for x in range(5): #looping over iterable
    values[x] = x * 2  # each iteration adding something to dict values

#this a line of code is exactly idential to above 3 lines
# whenever you have above pattern of code we can use dictionaries comprehensions
values = {x: x * 2 for x in range(5)}
print(values)

# Recap, We use comprehensions with list, set, dictionaries.

# but what about tuple
values = (x * 2 for x in range(5))
print(values)

# we get generator. What is generator?

