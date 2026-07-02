from math import factorial
from collections import Counter

def count_unique_vowel_strings(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    freq = Counter(s)

    vowel_freq = {ch: freq[ch] for ch in vowels if ch in freq}
    
    if not vowel_freq:
        return 0

    selection_ways = 1
    for count in vowel_freq.values():
        selection_ways *= count
    
    k = len(vowel_freq)
    permutation_ways = factorial(k)
    
    return selection_ways * permutation_ways


s = "aeiou"
print(count_unique_vowel_strings(s)) 
