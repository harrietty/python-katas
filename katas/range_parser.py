'''
In this Kata you are to implement a function that parses a string which is composed from tokens of the form 'n1-n2,n3,n4-n5:n6' where 'nX' is a positive integer. Each token represent a different range:

'n1-n2' represents the range n1 to n2 (inclusive in both ends). 'n3' represents the single integer n3. 'n4-n5:n6' represents the range n4 to n5 (inclusive in both ends) but only includes every other n6 integer.

The input string doesn't not have to include all the token types.
All integers are assumed to be positive.
Tokens may be separated by ',', ', ' or ,.
'''

import re

def range_parser(r):
  r = re.split('[,\s?|\.]+', r)

  def genSeq(instruction):
    step = None
    # match finds at the beginning of a string, search finds anywhere
    if re.search(':', instruction):
      in_split = re.split(':', instruction)
      step = int(in_split[1])
      instruction = in_split[0]

    if re.search(r'\-', instruction):
      instruction_range = re.split('-', instruction)
      beg = int(instruction_range[0])
      end = int(instruction_range[1])
      return list(range(beg, end + 1, (step or 1)))
    else:
      return [int(instruction)]
    
  return [y for z in [genSeq(x) for x in r] for y in z]