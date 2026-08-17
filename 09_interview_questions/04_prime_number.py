"""
Problem:
Prime Number

Difficulty:
Easy

Asked In:
TCS
Wipro
Infosys

Approaches:
1. Trial division up to n - 1
2. Trial division up to sqrt(n)

Time Complexity:
O(sqrt(n))

Space Complexity:
O(1)

Learning:
- Divisibility
- Why checking up to sqrt(n) is enough
- Edge cases: 0, 1, 2
"""

def is_prime_naive(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for value in [1, 2, 3, 4, 17, 18, 19]:
    print(value, is_prime(value))
