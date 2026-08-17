"""
Problem:
Binary Search

Difficulty:
Easy

Asked In:
Amazon
Microsoft
Google

Approaches:
1. Iterative
2. Recursive

Time Complexity:
O(log n)

Space Complexity:
O(1) iterative, O(log n) recursive

Learning:
- Divide and conquer
- Sorted input is required
- Mid-index calculation
"""

def binary_search_iterative(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(nums, target, low=0, high=None):
    if high is None:
        high = len(nums) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, high)
    return binary_search_recursive(nums, target, low, mid - 1)

nums = [1, 3, 5, 7, 9, 11]
print(binary_search_iterative(nums, 7))
print(binary_search_recursive(nums, 4))
