def linear_search(arr, target):
    pass
    # for (el, idx) in arr:
    #     print(el, '-', idx)
    #     if el == target:
    #         return idx

    # return -1   # not found

# arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# arr2 = []

# print(linear_search(arr1, 6), '-1')
# print(linear_search(arr1, -6), '8')
# print(linear_search(arr1, 0), '6')
# print(linear_search(arr2, 3), '-1')


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    if len(arr) > 0:
        while(arr[low] <= arr[high]):
            mid = low + (high-low) //2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                high = mid-1
            elif target > arr[mid]:
                low = mid+1
    else:
        return -1  # not found

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# arr2 = []

# print(binary_search(arr1, -8), '=1?')
# print(binary_search(arr1, 0), '=6?')
# print(binary_search(arr2, 6), '=-1?')
# print(binary_search(arr2, 0), '=-1?')