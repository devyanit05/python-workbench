"""
Problem:
Second Largest in a List

Difficulty:
Easy

Asked In:
Amazon
TCS
Infosys

Approaches:
1. One pass tracking first and second
2. Sort and pick the second unique value

Time Complexity:
O(n) one pass, O(n log n) sort

Space Complexity:
O(1)

Learning:
- Tracking two running values
- Duplicates of the largest value
- One pass vs sorting
"""

def second_largest_scan(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

def second_largest_sort(nums):
    unique = sorted(set(nums))
    return unique[-2]

print(second_largest_scan([3, 9, 1, 7, 2]))
print(second_largest_scan([10, 10, 9]))
print(second_largest_sort([10, 10, 9]))
