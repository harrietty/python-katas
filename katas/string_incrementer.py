# Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

import re
import math

def string_inc(st):
  match = re.search(r'[0-9]+$', st)
  if not match:
    return st + '1'
  else:
    g = match.group()
    print({'g': g, 'start': match.start()})
    zeroes_to_replace = re.match(r'0+', g)
    if zeroes_to_replace:
      zeroes_to_replace = len(zeroes_to_replace.group())
      g = g[zeroes_to_replace:]

    # handle if the ending numbers are all 000
    if g == '':
      zeroes_to_replace -= 1
      g = '0'
    
    next_num = int(g) + 1
    # handle if increasing by 1 overflows into another unit
    if next_num > 1 and math.floor(math.log10(next_num)) != math.floor(math.log10(next_num - 1)):
      if zeroes_to_replace == None: zeroes_to_replace = 0
      else: zeroes_to_replace -= 1
  
    return st[0:match.start()] + ('0' * zeroes_to_replace if (zeroes_to_replace != None and zeroes_to_replace > 0) else '') + str(next_num)