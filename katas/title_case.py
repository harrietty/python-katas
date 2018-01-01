# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# First argument (required): the original string to be converted.
# Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string

def title_case(str, exceptions = ''):
  if str == '': return str
  exceptions = [word.lower() for word in exceptions.split()]
  def make_title_case(word):
    if not word.lower() in exceptions:
      return word[0].upper() + word[1:].lower()
    else: 
      return word.lower()

  res = ' '.join([make_title_case(word) for word in str.split()])
  return res[0].upper() + res[1:]
