'''
Given a string, return the minimal number of parenthesis reversals needed to make balanced parenthesis.
'''

import math

def reverse_parens(st):
  if (not st) or len(st) % 2 != 0: return -1
  total = 0
  while '()' in st:
    st = st.replace('()', '')

  st = list(st)

  # Reverse first and last brackets if needed
  while len(st) > 0 and (st[0] == ')' or st[-1] == '('):
    if st[0] == ')':
      st[0] = '('
      total += 1
    if st[-1] == '(':
      st[-1] = ')'
      total += 1
    st = list(''.join(st).replace('()', ''))

  num_opening = st.count('(')
  num_closing = st.count(')')
  return total + math.ceil(abs(num_opening - num_closing)/2) 
