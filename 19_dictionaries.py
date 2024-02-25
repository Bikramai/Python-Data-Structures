point = {'x': 1, 'y': 2}
point = dict(x=1, y=2)  # better approch
point['x'] = 10
point ['z'] = 20

if 'a' in point: #check for the existance of key
    print(point['a'])

# other solution get method
print(point.get('a', 0)) # other way to check or get
del point['x'] # delete item
print(point)

# loop through dict
for key in point:
    print(key, point[key])

# another way to loop dict
for key, value in point.items():
    print(key, value)