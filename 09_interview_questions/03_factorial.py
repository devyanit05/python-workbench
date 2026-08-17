"""
Problem:
Factorial of a Number

Difficulty:
Easy

Asked In:
TCS
Infosys
Accenture

Approaches:
1. Loop
2. Recursion

Time Complexity:
O(n)

Space Complexity:
O(1) iterative, O(n) recursive

Learning:
- Accumulation in a loop
- Recursion and base cases
- 0! is 1
"""

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_iterative(5))
print(factorial_recursive(5))
