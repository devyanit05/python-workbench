"""
Problem:
Positive, Negative, or Zero

Difficulty:
Easy

Asked In:
TCS
Wipro
Accenture

Approaches:
1. if / elif / else
2. Nested comparisons

Time Complexity:
O(1)

Space Complexity:
O(1)

Learning:
- Conditional branching
- Zero is a separate case
- Comparison operators
"""

def classify(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

for value in [10, -7, 0]:
    print(value, classify(value))
