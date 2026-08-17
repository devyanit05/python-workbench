"""
Problem:
Fibonacci Sequence

Difficulty:
Easy

Asked In:
Amazon
Infosys
TCS

Approaches:
1. Loop
2. Recursion
3. Recursion with memoization

Time Complexity:
O(n) iterative, O(2^n) naive recursion

Space Complexity:
O(n)

Learning:
- Iteration vs recursion
- Overlapping subproblems
- Memoization
"""

def fibonacci_iterative(n):
    sequence = []
    a = 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}
    if n not in cache:
        cache[n] = fibonacci_memoized(n - 1, cache) + fibonacci_memoized(n - 2, cache)
    return cache[n]

n = 10
print(fibonacci_iterative(n))
print([fibonacci_recursive(i) for i in range(n)])
print([fibonacci_memoized(i) for i in range(n)])
