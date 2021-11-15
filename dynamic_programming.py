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
    if (m, n) in memo: return memo[m, n]
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1
    memo[m, n] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)  # no of ways column changes + no of ways row changes
    return memo[m, n]


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

def howsum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []  # numbers are non-negative
    if targetSum < 0: return None
    for i in numbers:
        compliment = targetSum - i
        compliment_array = howsum(compliment, numbers, memo)
        if compliment_array is not None:
            memo[targetSum] = [*compliment_array, i]
            return memo[targetSum]
    memo[targetSum] = None
    return memo[targetSum]


# print(howsum(7, [5, 3, 4, 7]))
# print(howsum(7, [2, 3]))
# print(howsum(8, [2, 3, 5]))
# print(howsum(300, [7, 14]))


def bestsum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    short_path = None
    for i in numbers:
        compliment = targetSum - i
        compliment_array = bestsum(compliment, numbers, memo)
        if compliment_array is not None:
            combo = [*compliment_array, i]
            if short_path is None:
                short_path = combo
                memo[targetSum] = short_path
            if len(short_path) > len(combo):
                short_path = combo
                memo[targetSum] = short_path
    memo[targetSum] = short_path
    return memo[targetSum]


# print(bestsum(7, [5, 3, 4, 7]))
# print(bestsum(8, [2, 3, 5]))
# print(bestsum(8, [1, 4, 5]))
# print(bestsum(100, [1, 2, 5, 25]))


def allsum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    short_path = None
    for i in numbers:
        compliment = targetSum - i
        compliment_array = bestsum(compliment, numbers, memo)
        if compliment_array is not None:
            combo = [*compliment_array, i]
            if short_path is None:
                short_path = [combo]
                memo[targetSum] = short_path
            else:
                if combo not in short_path and list(reversed(combo)) not in short_path:
                    short_path.append(combo)
                    memo[targetSum] = short_path
    memo[targetSum] = short_path
    return memo[targetSum]


# print(allsum(8, [10,1,2,7,6,1,5]))
# print(bestsum(100, [1, 2, 5, 25]))


def canconstruct(target, wordbank, memo={}):
    if target in memo: return memo[target]
    if target == "": return True
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):len(target)]
            if canconstruct(suffix, wordbank, memo):
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]


# print(canconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

def countconstruct(target, wordbank, memo={}):
    if target in memo: return memo[target]
    if target == "": return 0
    count = 0
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):len(target)]
            if canconstruct(suffix, wordbank):
                count += 1
                memo[target] = count
    return memo[target]


# print(countconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(countconstruct("purple", ["purp", "p", "ur", "le", "purpl"]))

def allconstruct(target, wordbank):
    if target == "": return []
    output = None
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):len(target)]
            suffix_array = allconstruct(suffix, wordbank)
            if suffix_array is not None:
                suffix_arrayas = [*suffix_array, word]
                if output is None:
                    output = [suffix_arrayas]
                output.append(suffix_arrayas)
    return output

# print(allconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(allconstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
