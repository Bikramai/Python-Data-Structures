point = ()
point = 1, 
point = 1, 2
point = (1, 2) + (3, 4)
print(type(point))
print('\n')

point = (1, 2) + (3, 4)
point = (1, 2) * 3
print(point)
print('\n')

point = tuple([1, 2]) # convert list to tuple we call tuple function
print(point)

point = tuple('Hello World') 
print(point)

point = (1, 2, 3)
print(point[0]) # similar like list we can access index in tuple
print(point[0:2]) # range of items
x, y, z = point # unpack the items
if 10 in point: # checks items but as we know this tuple are imutable
    print('exists')

# where is the real world we use tuple?
#here is the basic rule of thumb, 
# let's we dealing with sequencal of an objects and we want to make sure we don't 
# want to accidently modify the sequence, add new object to it or remove an existing objects, 
# instead we use tupble to prevent this accidental errors.
    