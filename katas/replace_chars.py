'''
In input string word(1 word):

replace the vowel with the nearest left consonant.
replace the consonant with the nearest right vowel.
P.S. To complete this task imagine the alphabet is a circle (connect the first and last element of the array in the mind). For example, 'a' replace with 'z', 'y' with 'a', etc.(see below)

The below constants are preloaded
'''

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']

def replace_chars(strng):
  if not strng: return ''

  def prevCon(ch):
    con = None
    ch_index = alphabet.index(ch)

    while con == None:
      ch_index -= 1
      if alphabet[ch_index] in consonants:
        con = alphabet[ch_index]    
    return con
  
  def nextVowel(ch):
    vowel = None
    ch_index = alphabet.index(ch)

    while vowel == None:
      ch_index = 0 if ch_index == len(alphabet)-1 else ch_index + 1
      if alphabet[ch_index] in vowels:
        vowel = alphabet[ch_index]
    return vowel

  return ''.join([prevCon(ch) if ch in vowels else nextVowel(ch) for ch in list(strng)])

  # Alternative: Use maketrans:
  # TR = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zeeediiihooooonuuuuutaaaaa')
