# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

import math

def comp(arr1, arr2):
  if len(arr1) != len(arr2): return False
  arr1.sort()
  arr2.sort()
  are_squares = [num == math.sqrt(arr2[i]) for i,num in enumerate(arr1)]
  return all(are_squares)