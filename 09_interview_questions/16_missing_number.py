"""
Problem:
Missing Number in 1..n

Difficulty:
Easy

Asked In:
Amazon
Microsoft
Adobe

Approaches:
1. Sum formula
2. XOR
3. Set difference

Time Complexity:
O(n)

Space Complexity:
O(1) sum / XOR, O(n) set

Learning:
- Gauss formula n * (n + 1) / 2
- XOR properties
- When extra space is acceptable
"""

def missing_sum(nums, n):
    expected = n * (n + 1) // 2
    actual = 0
    for num in nums:
        actual = actual + num
    return expected - actual

def missing_xor(nums, n):
    result = 0
    for i in range(1, n + 1):
        result ^= i
    for num in nums:
        result ^= num
    return result

def missing_set(nums, n):
    return (set(range(1, n + 1)) - set(nums)).pop()

print(missing_sum([1, 2, 4, 5], 5))
print(missing_xor([1, 2, 3, 4, 5, 6, 8], 8))
print(missing_set([1, 2, 4, 5], 5))
