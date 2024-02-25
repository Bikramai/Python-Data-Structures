#Fizz buzz alogorithm
# Here we have function fizz_buzz that takes an input depending on input we give it 
# it returns different results
""" here are the roles 
1.  if the input we give it is divisible by 3
    It will return string Fizz
2.  if the input we give it is divisible by 5
    It will return string Buzz
3.  if th input is divisible by both 3 and 5 (15)
    It will return string FizzBuzz
    For any other numbers it will returnsame input like 7 
    it will return 7"""

# sulution
# 1. checks input 
# technic #1
def fizz_buzz(input):
    if input % 3 == 0:
        result = 'Fizz'
    else: 
        result = 'Buzz'
    return result

print(fizz_buzz(5))
print('\n')

# technic #2
# There is better approach

def fizz_buzz(input):
    if input % 3 == 0:
        return 'Fizz'
    else: 
        return 'Buzz'

print(fizz_buzz(5))
print('\n')

# technic #3
# There is better approach

def fizz_buzz(input):
    if input % 3 == 0:
        return 'Fizz'
    return 'Buzz'

print(fizz_buzz(5))
print('\n')

# technic #4
# There is better approach

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz(15))