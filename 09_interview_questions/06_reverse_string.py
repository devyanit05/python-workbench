"""
Problem:
Reverse a String

Difficulty:
Easy

Asked In:
Amazon
Infosys
Accenture

Approaches:
1. Slicing
2. Loop
3. Stack

Time Complexity:
O(n)

Space Complexity:
O(n)

Learning:
- String slicing
- Iteration
- Immutable strings
"""

def reverse_slicing(s):
    return s[::-1]

def reverse_loop(s):
    reversed_text = ''
    for char in s:
        reversed_text = char + reversed_text
    return reversed_text

def reverse_stack(s):
    stack = list(s)
    reversed_text = ''
    while stack:
        reversed_text += stack.pop()
    return reversed_text

print(reverse_slicing('Python'))
print(reverse_loop('Python'))
print(reverse_stack('Devyani'))
