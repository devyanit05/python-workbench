"""
Problem:
Anagram

Difficulty:
Easy

Asked In:
Amazon
Microsoft
Infosys

Approaches:
1. Sort both strings
2. Frequency map

Time Complexity:
O(n log n) sort, O(n) frequency map

Space Complexity:
O(n)

Learning:
- Normalization (case and spaces)
- Sorting as a comparison trick
- Character counts
"""

def is_anagram_sort(left, right):
    def normalize(text):
        cleaned = []
        for char in text.lower():
            if char != ' ':
                cleaned.append(char)
        cleaned.sort()
        return cleaned

    return normalize(left) == normalize(right)

def is_anagram_frequency(left, right):
    def counts(text):
        freq = {}
        for char in text.lower():
            if char == ' ':
                continue
            freq[char] = freq.get(char, 0) + 1
        return freq

    return counts(left) == counts(right)

print(is_anagram_sort('listen', 'silent'))
print(is_anagram_frequency('Hello', 'world'))
print(is_anagram_frequency('Dormitory', 'Dirty room'))
