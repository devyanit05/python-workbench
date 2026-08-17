"""
Problem:
Even or Odd

Difficulty:
Easy

Asked In:
TCS
Infosys
Accenture

Approaches:
1. Modulo
2. Bitwise AND

Time Complexity:
O(1)

Space Complexity:
O(1)

Learning:
- Remainder operator
- Least significant bit is 0 for even numbers
"""

def even_or_odd_modulo(n):
    if n % 2 == 0:
        return 'Even'
    return 'Odd'

def even_or_odd_bitwise(n):
    if n & 1 == 0:
        return 'Even'
    return 'Odd'

for value in [0, 1, 2, 7, 10]:
    print(value, even_or_odd_modulo(value), even_or_odd_bitwise(value))
