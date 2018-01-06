def product_of_parts(nm):
  nm = str(nm)

  combos = []

  for i in range(0, len(nm)-2):
    for j in range(i+1,len(nm)-1):
      combos.append([int(nm[0:i+1]), int(nm[i+1:j+1]), int(nm[j+1:])])
  
  def mult(ar):
    sum = 1
    for elem in ar:
      sum = elem * sum
    return sum

  return max([mult(nums) for nums in combos])
