values = [x * 2 for x in range(10)]
for x in values:
    print(x)
print('\n')



# There will be the suitation we will be working with very 
# large data set or pheraph infinite set of data. 
# In this case, we shouldn't store all the data to the memory, if the data
# is millions or billions. In this case we use generator object.
# Generator objects are iterable just like list. Each generator generates the new 
# values, on like list, they don't store all the values in memory. They generates 
# new values in each iteration. lets see how generator works


# values = (x * 2 for x in range(10))
# print(values)
# for x in values:
#     print(x)

# however value is nolonger list. It is generator object
    
from sys import getsizeof

values = (x * 2 for x in range(1000000)) # generator expression
print(('gen:', getsizeof(values)))

values = [x * 2 for x in range(1000000)] #list 
print(('list:', getsizeof(values)))

