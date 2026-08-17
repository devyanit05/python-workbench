"""
Problem:
Frequency Counter

Difficulty:
Easy

Asked In:
Amazon
Infosys
Accenture

Approaches:
1. Dictionary
2. collections.Counter

Time Complexity:
O(n)

Space Complexity:
O(k) where k is the number of unique items

Learning:
- Hash maps
- Counting occurrences
- Dictionary get() / membership
"""

from collections import Counter

def frequency_dict(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts

def frequency_counter(items):
    return dict(Counter(items))

print(frequency_dict('Devyani'))
print(frequency_counter(['Python', 'Java', 'Python', 'C++', 'Python']))
