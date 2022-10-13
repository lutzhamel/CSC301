# compute a list whose elements are incremented
# by one compared to the input list

a = [1,2,3]
b = []

# using map
b = list(map((lambda x : x+1), a))

assert(b == [2,3,4])
