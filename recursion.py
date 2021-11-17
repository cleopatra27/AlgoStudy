def sum(numbers):
    # base case
    if not numbers: return 0
    remain = sum(numbers[1:])
    return numbers[0] + remain

print(sum([1,2,3,4,5]))
