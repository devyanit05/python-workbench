"""
Problem:
Sum of First N Natural Numbers

Difficulty:
Easy

Asked In:
TCS
Infosys
Wipro

Approaches:
1. Loop
2. Formula n * (n + 1) / 2
3. Recursion

Time Complexity:
O(n) loop, O(1) formula

Space Complexity:
O(1) loop / formula, O(n) recursion

Learning:
- Accumulation
- Closed-form formula
- Recursion vs constant-time math
"""

def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

def sum_formula(n):
    return n * (n + 1) // 2

def sum_recursive(n):
    if n <= 1:
        return n
    return n + sum_recursive(n - 1)

print(sum_loop(10))
print(sum_formula(100))
print(sum_recursive(10))
