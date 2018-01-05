import collections

def only_duplicates(s):
  c = collections.Counter(s)
  return ''.join([ch for ch in s if c[ch] != 1])