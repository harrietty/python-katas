'''
return a string where:
1) the first and last characters remain in original place for each word
2) characters between the first and last characters must be sorted alphabetically
3) punctuation should remain at the same place as it started, for example: shan't -> sahn't
'''

import re

def scramble(strng):
    if len(strng) < 2:
        return strng
    strng = strng.lower().split()

    def orderMiddleChars(s):
        firstCh = re.search(r'^[^a-z]*\w', s).group()
        lastChr = re.search(r'\w[^a-z]*$', s).group()
        middleChars = list(s[len(firstCh):-len(lastChr)])
        sortedMiddleChars = sorted([x for x in middleChars if x.isalpha()])

        for i,ch in enumerate(middleChars):
            if re.match(r'[a-z]', ch):
                middleChars[i] = sortedMiddleChars.pop(0)

        return firstCh + ''.join(middleChars) + lastChr
    
    return ' '.join([orderMiddleChars(s) for s in strng])