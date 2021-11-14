'''
This is a programming flow that either uses iteration or recursion to find a solution'
It does this by solving a problem bit by bit.
And can either use memoization or tabulation to saved solved bits

TIP: start with a brute force recursive approach first before adding memoization or tabulation to save solved bits
Recipe:
    First figure out how to draw this in a tree :- visualize
    Take note of the base cases :- repeated nodes
    Implement the tree using recursion
    Test the brute force solution
    Then make it efficient using a memo object; decide what the key for your meo will be, preferably the inputs if nt an array
    Add memo base case :- check if arguments are already in your memo object; return that
    return the memo object needed

What types of questions to use dynamic programming?

Recursion - memoization examples:
'''


def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(50))


def gridTraveler(m, n, memo=None):
    # base case
    if memo is None:
        memo = {}
    if (m,n) in memo: return memo[m,n]
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1
    memo[m,n] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1) # no of ways column changes + no of ways row changes
    return memo[m,n]

# print(gridTraveler(2, 3))
# print(gridTraveler(18, 18))


def cansum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False
    for i in numbers:
        compliment = targetSum - i
        if cansum(compliment, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


# print(cansum(7, [5, 3, 4, 7]))
# print(cansum(7, [2, 4]))
# print(cansum(300, [7, 14]))

def howsum(targetSum, numbers):
    if targetSum == 0: return [] # numbers are non-negative
    if targetSum < 0: return []
    for i in numbers:
        compliment = targetSum - i
        compliment_array = howsum(compliment, numbers)
        print(len(compliment_array))
        if compliment_array is not None:
            return compliment_array
    return [None]


print(howsum(7, [5, 3, 4, 7]))