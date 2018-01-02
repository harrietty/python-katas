# There is an array with some numbers. All numbers are equal except for one. Try to find it!

import collections

def find_unique(arr):
  c = collections.Counter(arr)
  return next(num for num in c if c[num] == 1)