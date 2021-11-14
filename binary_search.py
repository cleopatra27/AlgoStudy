'''
Linear search is a search that finds an element in the list by searching the element sequentially until the element is found in the list.
On the other hand, a binary search is a search that finds the middle element in the list recursively until the middle element is matched with a searched element.

That is, for an array [1, 2, 3, 4, 5, 6], instead of searching through each element in the array,
we find the middle ( 1 + 6) // 2 = 3,
then compare it to whichever condition suits the problem,
we can then either go right of the now divided array,
by adding one to the mid or
go left by subtracting one from the mid
until we find the value based on the condition we are looking for.

NB: This works only on a sorted array
'''


def search(aray, length, key):
    low = 0
    high = length
    while low < high:
        mid = (low + high) // 2
        if key == aray[mid]:  # condition 1
            return mid
        if key < aray[mid]: # condition 2
            high = mid # use the lower bound section of the array
        else:
            low = mid + 1 # use the higher bound section of the array
    return 0


array = [1, 2, 3, 4, 5, 6]
print(search(array, len(array), 6))


'''
A sample application on this is finding square root of a number, as below:
'''
# TO DO: return this with the decimal place

def sqrt(number):
    low, high =0, number + 1
    while low < high:
        mid = (low + high) // 2
        if mid * mid > number:
            high = mid
        else:
            low = mid + 1
    return low - 1

# print(sqrt(199))
