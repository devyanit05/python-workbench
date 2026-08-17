"""
Problem:
String Length without len()

Difficulty:
Easy

Asked In:
TCS
Infosys
Wipro

Approaches:
1. Loop
2. Recursion

Time Complexity:
O(n)

Space Complexity:
O(1) loop, O(n) recursion

Learning:
- Iteration over a string
- Recursion on slices
- Why len() exists
"""

def length_loop(text):
    count = 0
    for _ in text:
        count = count + 1
    return count

def length_recursive(text):
    if text == '':
        return 0
    return 1 + length_recursive(text[1:])

print(length_loop('Python'))
print(length_recursive('Devyani'))
