"""
Problem:
Maximum in a List

Difficulty:
Easy

Asked In:
Amazon
Infosys
Accenture

Approaches:
1. Linear scan
2. Sort and pick the last element

Time Complexity:
O(n) scan, O(n log n) sort

Space Complexity:
O(1) scan

Learning:
- Linear search
- Why a single pass is enough
- Avoid using max() in interviews
"""

def maximum_scan(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

def maximum_sort(nums):
    return sorted(nums)[-1]

print(maximum_scan([3, 9, 1, 7, 2]))
print(maximum_scan([-5, -1, -12]))
print(maximum_sort([3, 9, 1, 7, 2]))
