# Part 1 of Esolang kata series
# https://www.codewars.com/kata/esolang-interpreters-number-1-introduction-to-esolangs-and-my-first-interpreter-ministringfuck

import re

def parse_esolang(st):
  st = re.findall(r'\++|\.', st)
  memory = 0

  chars = ''
  for i,instr in enumerate(st):
    if instr == '.': chars += chr(memory)
    else:
      memory = (memory + len(instr)) % 256
  
  return chars