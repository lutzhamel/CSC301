# compute a list whose elements are incremented
# by one compared to the input list

a = [1,2,3]
b = []

# iterate over the list
for e in a:
  b.append(e+1)

assert(b == [2,3,4])
