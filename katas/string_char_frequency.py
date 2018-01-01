# In this Kata, we are going to determine if the count of each of the characters in a string can be equal if we remove a single character from that string.

from collections import Counter

def string_char_frequency(str):
  tally = Counter(str) # => {'o': 2, 'b': 2, 'c': 2, 'f': 1}
  counts = Counter(tally.values()) # => {2: 3, 1: 1}
  min_val = min(counts.values()) # value represents how many groups of the given number of repeats
  min_key = min(counts.keys()) # key represents the number of repeated characters
  max_key = max(counts.keys())

  return (len(counts) == 2 and min_key == 1 and counts[min_key] == 1) or (len(counts) == 2 and min_val == 1 and max_key - min_key == 1) or (len(counts) == 1 and min_key == 1) or (len(counts) == 1 and min_val == 1)
