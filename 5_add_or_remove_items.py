letters = ['a', 'b', 'c']

# Add
letters.append('d') # at end
letters.insert(0, '-') # add the item in the given index, or where ever we want.
print(letters)

# Remove 
letters.pop() # remove the item at the end
letters.pop(0) # remove the item in the given index, or where ever we want.
letters.remove('b') # remove the item but you dont know the index, if thats case
del letters[0:3] # delete item with index and range of items
letters.clear() # if you want to delete all items or object from the list
print(letters) 


