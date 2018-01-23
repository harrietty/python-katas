'''
Given a list of lists containing only 1s and 0s, return a new list that differs from list 1 in its first element, list 2 in its second element, list 3 in its 3rd element, and so on
'''

def cantor(arr):
    return [not(line[i]) for i,line in enumerate(arr)]