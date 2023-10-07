# sum the integer values on a list

def listsum(l):
  match l:
    case [] :
      return 0
    case (h,*t) :
      return h+listsum(t)

assert(listsum([1,2,3]) == 6)


