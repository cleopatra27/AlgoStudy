def merge_sort(array):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Finds the mid point of th elist and divide into sub lists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sub lists created in previous step.

    Takes O(n log n)
    :param array:
    :return:array:
    """

    # base cases
    if len(array) <= 1: return array

    left_half, right_half = split(array)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    :param list:
    :return: two sublists - left and right
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:] # O(k)
    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    :param left:
    :param right:
    :return: list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # when right is shorter than left
    while i < len(left):
        l.append(left[i])
        i += 1

    # when left is s shorter than right
    while j < len(right):
        l.append(right[j])
        j += 1

    return l


# array = [9, 3, 7, 5, 6, 4, 8, 2]
# print(merge_sort(array))

def verify(list):
    n = len(list)

    if n == 0 or n ==1:
        return True

    return list[0] < list[1] and verify(list[1:])


array = [9, 3, 7, 5, 6, 4, 8, 2]
l = merge_sort(array)
print(verify(l))