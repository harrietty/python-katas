# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

from functools import reduce

def persistence(num):
  if num < 10: return 0
  
  def multiply(arr):
    return reduce(lambda total,n: total * n, arr)
  
  loops = 0
  while num >= 10:
    loops += 1

    # Create array of individual integers from the number
    s = [int(n) for n in str(num)] 

    # num = Multiply all integers together
    num = multiply(s)

  return loops