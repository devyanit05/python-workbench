"""
Problem:
Palindrome

Difficulty:
Easy

Asked In:
Amazon
Accenture
Infosys

Approaches:
1. Slicing
2. Loop
3. Two pointers

Time Complexity:
O(n)

Space Complexity:
O(n) slicing, O(1) two pointers on a sequence

Learning:
- String reversal
- Two-pointer technique
- Works for both strings and numbers
"""

def is_palindrome_slicing(value):
    text = str(value)
    return text == text[::-1]

def is_palindrome_loop(value):
    text = str(value)
    reversed_text = ''
    for char in text:
        reversed_text = char + reversed_text
    return text == reversed_text

def is_palindrome_two_pointers(value):
    text = str(value)
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

for value in ['level', 'Python', 121, 123]:
    print(value, is_palindrome_two_pointers(value))
