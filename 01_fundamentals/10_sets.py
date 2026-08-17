# ------------------------------------------------------------------------
# Sets
# ------------------------------------------------------------------------
# Sets are unordered collections of unique elements.
# They are mutable but cannot contain mutable elements like lists or dictionaries.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)

set3 = set2
print(set3)

set5 = {'Python', 'TypeScript', 'C#', 'JavaScript'}
print(set5)

set6 = {'Python', 'Java', 'C++', 'JavaScript', 'Python'}  # duplicates are removed
print(set6)

print('Python' in set5)
print('TypeScript' in set6)

print(set5.intersection(set6))
print(set5.difference(set6))
set4 = set1.union(set2)
print(set4)

set5.add('Go')
print(set5)

# {} creates an empty dictionary, not a set
empty_set = set()
print(empty_set)
