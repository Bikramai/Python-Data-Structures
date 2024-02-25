items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]


prices = list(map(lambda item:item[1], items)) # using map list function
# The prepare way to Map and Filter list in python community is to use list comprehensions 
prices = [item[1] for item in items] # Using list comprehensions


filtered = list(filter(lambda item: item[1] >= 10, items)) # using filtered list 
[item for item in items if item[1] >= 10]  #Using list comprehensions