"""
Problem:
Bubble Sort

Difficulty:
Easy

Asked In:
TCS
Infosys
Wipro

Approaches:
1. Naive nested loops
2. Optimized with a swapped flag

Time Complexity:
O(n^2)

Space Complexity:
O(1)

Learning:
- Adjacent swaps
- Early exit when already sorted
- Stable sorting
"""

def bubble_sort(nums):
    values = list(nums)
    n = len(values)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break
    return values

print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([3, 3, 1]))
