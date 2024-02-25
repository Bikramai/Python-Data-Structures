# common question microsoft, amazon, google ask a lots
# Find the most repeated charcters in the sentence?

# How do we solve this problem
"""
1. We need to know how many times each character is repeated.
once we have this information then we can find most characters.

2. We need to know what kind of datas structure is useful for storaging
this information? - A Dictionary :- dictionary is collections of key value pairs
- so here we can use character as the key and repeation as value
"""
from pprint import pprint
sentence = "This is a commomn interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1) # width determines the numbers of character in each line.
# If that function doesn't fit. This function will add line break. This is the better way to print dict
        
# Now we have all the information to solve the problem. Next step is to sorted in dictionary by the frequency of characters

char_frequency_sorted = sorted(
    char_frequency.items(), 
    key=lambda kv: kv[1], 
    reverse=True)
print(char_frequency_sorted[0])



