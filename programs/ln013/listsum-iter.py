# sum the integer values on a list

def listsum(l):
   acc = 0
   for v in l:
      acc += v
   return acc

assert(listsum([1,2,3]) == 6)


