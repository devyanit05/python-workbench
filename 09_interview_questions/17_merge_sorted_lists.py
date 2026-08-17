"""
Problem:
Merge Two Sorted Lists

Difficulty:
Easy

Asked In:
Amazon
Microsoft
Google

Approaches:
1. Two pointers
2. Concatenate and sort

Time Complexity:
O(n + m) two pointers, O((n + m) log(n + m)) sort

Space Complexity:
O(n + m)

Learning:
- Two-pointer technique
- Preserving sorted order
- Why merging is cheaper than sorting again
"""

def merge_two_pointers(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1
    while i < len(left):
        merged.append(left[i])
        i = i + 1
    while j < len(right):
        merged.append(right[j])
        j = j + 1
    return merged

def merge_sort(left, right):
    return sorted(left + right)

print(merge_two_pointers([1, 3, 5], [2, 4, 6]))
print(merge_sort([1, 2, 7], [3]))
