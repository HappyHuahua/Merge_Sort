import math


def mergesort(array):
    if len(array) < 2:
        return array
    middle = math.floor(len(array) / 2)
    left, right = array[0:middle], array[middle:]
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res


if __name__ == '__main__':
    arr1 = input("Input array: ")
    A = [int(n) for n in arr1.split()]
    result = mergesort(A)
    print(result)
