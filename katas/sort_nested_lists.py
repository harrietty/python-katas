'''
You get some nested lists. Keeping the original structures, sort only elements (integers) inside of the lists. In other words, sorting the intergers only by swapping their positions.

Example
Input   : [[[2, 1], [4, 3]], [[6, 5], [8, 7]]]
Output  : [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
Note: The structures of the lists are regular (symmetrical) and their depths are 3.
'''

import itertools

def sort_nested(lst):
  # create a flattened, sorted list
  # global sorted_nums
  sorted_nums = list(itertools.chain(*list(itertools.chain(*lst))))
  sorted_nums.sort()

  # for each item in a nested list, pop a num off the sorted list to replace it.

  def sort_inner_lists(l):
    def replace_nums(ar):
      nonlocal sorted_nums
      sliced = sorted_nums[0:len(ar)]
      sorted_nums = sorted_nums[len(ar):]
      return sliced
    return [replace_nums(inner)for inner in l]

  return [sort_inner_lists(l) for l in lst]

'''
NB GLOBAL VARS: Python assumes that any name that is assigned to, anywhere within a function, is local to that function unless explicitly told otherwise. If it is only reading from a name, and the name doesn't exist locally, it will try to look up the name in any containing scopes (e.g. the module's global scope).
'''