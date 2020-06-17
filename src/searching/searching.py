def linear_search(arr, target):
    # Your code here
    for n in range(0, len(arr)):
        if arr[n] == target:
            return n

    return -1   # not found

print(linear_search([3,5,2,1,4,8,9,7,6], 6))





# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here


    return -1  # not found

print(binary_search([3,5,2,1,4,8,9,7,6], 6))