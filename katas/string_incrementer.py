# Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

import re

def string_inc(st):
  # get the beginning of the str, pre-final nums
  beg = st.rstrip('0123456789')

  # get the final num sequence
  end = re.search(r'[0-9]+$', st)
  
  # if there are no nums at the end, append 1
  if not end: return beg + '1'

  # return beginning + incrememented number, zfilled to correct length
  
  return beg + str(int(end.group()) + 1).zfill(len(end.group())) 