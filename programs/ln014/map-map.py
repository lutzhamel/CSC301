# compute a list whose elements are incremented
# by one compared to the input list

a = [1,2,3]
b = []

# using map
b = map((lambda x : x+1), a)

assert(list(b) == [2,3,4])
