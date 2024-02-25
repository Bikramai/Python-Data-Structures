items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]
#1st args:
# lambda function takes an item and return a boolean value that determine if this items matches criteria or not.
# In this case, we want to get price of each item and see that greater(>) equal (=) to 10
# The result of this expression is boolean value , if it is True item will return 

#2nd args:
# we passed the items list
# better option is built in filter function and filter object is just like map object. 
# It is iterable so 
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)