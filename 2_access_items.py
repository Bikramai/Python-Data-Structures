letters = ['a', 'b', 'c', 'd']
letters[0] = 'A'
print(letters[0])
print(letters[-1])

print(letters[0:3]) 
print(letters[:3])

print(letters)
print(letters[0:])  # New list with the all the items in original list

print(letters[:])  # copy of the original list

print(letters[::2])


numbers = list(range(20)) 
print(numbers[::2]) # taking out eveery items of the original list
print(numbers[::3]) #taking out every two items from the original list
print(numbers[::4]) #taking out every 3 items from the original list
print(numbers[::5])
print(numbers[::6])
print(numbers[::7])

print(numbers[::-1]) #write in reverse order

