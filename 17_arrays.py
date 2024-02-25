"""if you are dealing with large sequence of numbers, we have more efficient 
- data types python called Arrays. This arrays takes less memories and perform 
  little bit faster.
- But note that we will only see when we deal with large numbers lets say 10,000 or more.
- 90% of case we will use list but if you see performance problems than we can see if you can solve 
- by replacing the list with arrays. If you don't have a perforance problem don't try to optimize.
- Don't solve the problems that doesn't exist.
- use array only when you are dealing with large sequence numbers and encunter perforance problems.
"""

from array import array

numbers = array('i', [1, 2, 3])
numbers[0] = 1.0
