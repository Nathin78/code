# Check if two strings are anagrams
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram_sort("listen", "silent"))  # True
