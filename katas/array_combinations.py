# In this Kata, you will be given an array of arrays and your task will be to return the number of unique arrays that can be formed by picking exactly one element from each subarray. 
from functools import reduce

def array_combs(arrs):
    # remove any duplicates from each array and then multiply their lengths
    
    arrs = [set(subarr) for subarr in arrs]
    
    return reduce(lambda x,y:
        x * len(y) if type(x) == int
        else len(x) * len(y), arrs)