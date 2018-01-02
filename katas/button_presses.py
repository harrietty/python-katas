''' 
For this assignment, write a module that can calculate the amount of button presses required for any phrase. Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters (but you should allow your module to accept input in either for convenience).
 ------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------
'''

import re

def button_presses(s):
  keys = [(1, None), (2, 'abc'), (3, 'def'), (4, 'ghi'), (5, 'jkl'), (6, 'mno'), (7, 'pqrs'), (8, 'tuv'), (9, 'wxyz'), ('*', None), (0, ' '), ('#', None)]

  def find_presses_for_char(char):
    if re.match(r'[#*]', char):
      return 1
    if re.match(r'\d', char):
      # for a number, find the key and the presses = chars.length + 1
      selected_num = next(t for t in keys if t[0] == int(char))
      return 1 if selected_num[1] == None else len(selected_num[1]) + 1
    else:

      # for a letter, find which key contains the letter 
      selected_key = next(t for t in keys if t[1] != None and char.lower() in t[1])
      # how many presses does it take?
      return selected_key[1].find(char.lower()) + 1

  presses = [find_presses_for_char(ch) for ch in list(s)]

  return sum(presses)