# The call stack with recursion
# Recursive functions use the call stack too! Let’s look at this 
# in action with the factorial function. factorial(5) is
# written as 5!, and it’s defined like this: 5! = 5 * 4 * 3 * 2 * 1.
# Similarly, factorial(3) is 3 * 2 * 1. Here’s a recursive
# function to calculate the factorial of a number:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))    