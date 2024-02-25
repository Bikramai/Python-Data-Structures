list1 = [1, 2, 3]
list2 = [11, 22, 33]

# how can we make it tuple
[(1, 11), (2, 22), (3, 30)]

# By using Zip built-in fuction
print(list(zip('abc', list1, list2))) # we can also pass string 