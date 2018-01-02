# There is an array of strings. All strings contains similar letters except one. Try to find it!

import collections

def find_uniq_string(arr):
  def organise(str):
    '''
    Returns a string of chars in alphabetical order, lowercase, with any duplicates and spaces removed
    '''
    s = set(str.lower())
    if ' ' in s: s.remove(' ')
    return ''.join(sorted(list(s)))

  organised_arr = [organise(s) for s in arr]
  c = collections.Counter(organised_arr)
  unique_chars = next(st for st in c if c[st] == 1)
  return next(s for s in arr if unique_chars == organise(s))
