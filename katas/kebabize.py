# Complete the kebabize function so that it converts a camel case string into a kebab case. the returned string should only contain lowercase letters

import re

def kebabize(strng):
  # findall produces an array of matches
  strng = re.sub(r'\d+', '', strng)
  strng = re.findall(r'([A-Z]?[a-z]+)|([A-Z])', strng)
  return '-'.join([w[0].lower() if w[0] else w[1].lower() for w in strng])