"""
Problem:
Armstrong Number

Difficulty:
Easy

Asked In:
TCS
Infosys
Capgemini

Approaches:
1. Convert to string and loop over digits
2. Extract digits with modulo

Time Complexity:
O(d) where d is the number of digits

Space Complexity:
O(1)

Learning:
- Digit extraction
- Powers
- 153 = 1^3 + 5^3 + 3^3
"""

def is_armstrong_string(n):
    digits = str(n)
    power = 0
    for _ in digits:
        power = power + 1
    total = 0
    for digit in digits:
        total = total + int(digit) ** power
    return total == n

def is_armstrong_modulo(n):
    original = n
    digits = 0
    temp = n
    if temp == 0:
        digits = 1
    while temp > 0:
        digits += 1
        temp //= 10
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total == original

for value in [153, 370, 371, 9474, 123]:
    print(value, is_armstrong_string(value))
