"""
Problem:
Swap Two Numbers (without a temp variable)

Difficulty:
Easy

Asked In:
TCS
Infosys
Wipro

Approaches:
1. Tuple unpacking
2. Arithmetic
3. XOR

Time Complexity:
O(1)

Space Complexity:
O(1)

Learning:
- Tuple unpacking
- Arithmetic swap
- XOR swap
"""

def swap_unpacking(a, b):
    a, b = b, a
    return a, b

def swap_arithmetic(a, b):
    try:
        a = a + b
        b = a - b
        a = a - b
        return a, b
    except TypeError:
        return 'Invalid input'

def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

print(swap_unpacking(100, 20))
print(swap_arithmetic(100, 20))
print(swap_xor(100, 20))
