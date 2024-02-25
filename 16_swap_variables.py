x = 10
y = 20

z = x
x = y
y = z

print('x', x)
print('y', y)
print('\n')

# Better approch
x, y = y, x   # we are defining a tuple which is equalvant to x, y =(10, 20), unpacking left side

print('x', x)
print('y', y)