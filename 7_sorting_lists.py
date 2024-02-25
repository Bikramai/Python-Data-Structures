numbers = [3, 51, 89, 2, 9, 6, 5]
numbers.sort() # sorting in accending order
# numbers.sort(reverse=True) # sorting decending order
print(sorted(numbers, reverse=True)) #buitl in function and takes any iterable and sorted
print(numbers)
print('\n')


items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# Clean way to do this method in Lambda function