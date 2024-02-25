browsing_session = []
browsing_session.append(1) # we use append to add an item to top of stacks
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop() # to remove the top of the stacks
print(last)
print(browsing_session)
print('redirect', browsing_session[-1])

# Falsey value
# 0
# ''
# []

if not browsing_session:
    print('disable')


# Recap, this are the operations that we perform in the stacks
browsing_session = []
browsing_session.append(1) # we use append to add an item to top of stacks
last = browsing_session.pop() # to remove the top of the stacks
if not browsing_session: # to check to see empty or not
    browsing_session[-1] # we use -1 index to get an item to top of the stacks

