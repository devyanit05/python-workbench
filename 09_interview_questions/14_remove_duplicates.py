"""
Problem:
Remove Duplicates from a List

Difficulty:
Easy

Asked In:
Amazon
Infosys
Accenture

Approaches:
1. Loop with a seen list (keeps order)
2. set() (order not guaranteed on older Python)
3. dict.fromkeys() (keeps order)

Time Complexity:
O(n) with a set / dict, O(n^2) with a list

Space Complexity:
O(n)

Learning:
- Membership tests
- Order preservation
- set vs list for lookups
"""

def remove_duplicates_loop(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

def remove_duplicates_dict(items):
    return list(dict.fromkeys(items))

print(remove_duplicates_loop([1, 2, 2, 3, 1, 4]))
print(remove_duplicates_dict(['Python', 'Java', 'Python', 'C++']))
