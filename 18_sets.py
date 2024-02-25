'''
Set is the collection with no duplicate and we use curly brackets to define
set. unlike list with unorder collection which means the items on our sets 
are not in sequence, so we cannot access them using index
'''

numbers = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5 ]
first = set(numbers)
second = {1, 6, 7, 8, 9}
# second.add(5)
# second.remove(5)
# len(second) # length function 

print(first | second) # union of the set
print(first & second) # intersection of set
print(first - second) # difference between set, first set has additional num we dont have in second
print(first ^ second) # this will return the items that are either first or second sets but not both

# set quit often we use one of operators here or we can check for the existance of the item in a set.

if 1 in first:
    print('yes')