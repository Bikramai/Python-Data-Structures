letters = ['a', 'b', 'c']
for letter in enumerate(letters):  # each iteration, enumerate items will gives us tuple, tuple is the list and read only -index and item
    print(letter[0], letter[1]) # so we will see index and items


# Clean method
letters = ['a', 'b', 'c']
# items = [0, 'a']
# index, letter = items

for index, letter in enumerate(letters):  
    print(index, letter)
    