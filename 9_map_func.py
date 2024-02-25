items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

# Let's transform/Map this into our original list of numbers that is list of prices
prices = []
for item in items:
    prices.append(item[1])

print(prices)
print('\n')

# There is more better and aligant way to acheive the same result.
# that is Map built-in function 

prices = list(map(lambda item:item[1], items)) # convert map to list function
print(prices)