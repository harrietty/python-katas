'''
In this kata you're given an n x n array and you're expected to traverse the elements diagonally from the bottom right to the top left.

Example
  1 6 7
  7 2 4
  3 5 9
your solution should return elements in the following order

9
4 5
7 2 3
6 7
1
'''

import itertools
import math

def diagonally(arr):

  ## flatten array by unpacking list and chaining
  arr = list(itertools.chain(*arr))
  length = len(arr)

  # start at last index
  finali = length - 1

  def getNums(n):
    if n == length-1:
      return [arr[n]]
    r = []
    while n < length-1:
      r.append(arr[n])
      n += (int(math.sqrt(length)) - 1)
    return r

  def getNNums(n):
    '''
    if given 3, will get index 3 plus the subsequent 3 n+2 indexes
    '''
    target_length = n + 1
    r = []
    while len(r) < target_length:
      r.append(arr[n])
      n += (int(math.sqrt(length)) - 1)
    return r


  res = []
  
  # Starting from bottom right to top right
  for i in range(finali, -1, -int(math.sqrt(length))):
    res = res + getNums(i)
  

  # And from top right to top left
  topright = int(math.sqrt(length)) - 2
  for i in range(topright, -1, -1):
    res = res + getNNums(i)

  return res